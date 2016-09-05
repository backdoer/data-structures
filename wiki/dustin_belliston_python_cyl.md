This coding example takes a local directory and uploads it to an AWS S3 bucket.

The code will also use the **tinify** library to compress any images in the folder. If you just want to upload a directory, you can do this with boto3 *sync* function.

##Get set up:

```python
#! /usr/local/bin/python3

import os
import sys
import boto3
import botocore
import argparse
import tinify
```

##Store extensions I want to look at for
```python
IMAGE_EXT = ['.png', '.jpg', '.jpeg']
IGNORE_EXT = ['', '.DS_STORE']
```

##Use arg parser to pull arguments into variables
```python
def main(argv):
    parser = argparse.ArgumentParser(description='Folder upload to AWS')
    parser.add_argument('-b', '--bucket',
                        help='Target Bucket Name', required=True)
    parser.add_argument('-s', '--source',
                        help='Source Folder', required=True)
    parser.add_argument('-tiny', '--tiny',
                        help='Tinify Key', required=True)
    parser.add_argument('-d', '--destination',
                        help='Destination Folder', required=False)
    args = parser.parse_args()

    tinify.key = args.tiny
```

##See boto3 documentation for this info. Basically setting up a session.
```python
    # Use set destination or just name of directory being uploaded
    destination_path = args.destination if args.destination else args.source.split('/')[-1]
    print('***Uploading {} to s3://{}/{} ...'.format(args.source, args.bucket, destination_path))

    # Client + Resource + Waiters
    session = boto3.session.Session()
    client = session.client('s3')
    s3 = session.resource('s3')
    all_buckets = s3.buckets.all()
    waiter_bucket_exists = client.get_waiter('bucket_exists')
```

##Making sure we have the bucket the user wants to upload to
```python
    # Get or create the target bucket
    if all_buckets:
        target_bucket = next((cb for cb in all_buckets
                             if cb.name == args.bucket), None)

    if target_bucket is None:
        client.create_bucket(Bucket=args.bucket)

    waiter_bucket_exists.wait(Bucket=args.bucket)
```

##This code using the **os** library to walk the directory
```python
    # Walk os and upload files one at a time
    for root, dirs, files in os.walk(args.source):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if ext in IGNORE_EXT:
                pass
            else:
                # Set the path relative to the source directory, we dont want to grab the full path
                rel_path = os.path.relpath(os.path.join(root, file), args.source)
                s3_path = os.path.join(destination_path, rel_path)                

                if ext in IMAGE_EXT:
                    source = tinify.from_file(os.path.join(root, file))
                    # tinify will place the file into s3 natively
                    source.store(
                        service="s3",
                        aws_access_key_id=session.get_credentials().access_key,
                        aws_secret_access_key=session.get_credentials().secret_key,
                        region=session.region_name,
                        path="{}/{}".format(args.bucket, s3_path)
                    )

                # Upload the file with the S3 client
                client.upload_file(os.path.join(root, file), args.bucket, s3_path)

    print('Complete.')
```

##
```python
if __name__ == "__main__":
    main(sys.argv[1:])
```
