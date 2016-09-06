My example will show how easy it is to build a simple brute-force password cracker in Python.

## Import necessary libraries
This example will use three of the Python's standard libraries (modules)

```python
import crypt, time, optparse
```
Crypt provides an "interface to the crypt(3) routine, which is a one-way hash function based upon a modified DES algorithm". In other words, it allows us to do things like hashing passwords or attempt to crack Unix passwords using a dictionary, which is exactly what we'll be doing.

Time gives us access to any time-related functions, but we'll only use sleep() for this example.

Optparse allows to us to parse command-line arguments in a easy-to-read format.


## Parse command-line args

```python
  parser = optparse.OptionParser('usage %prog -d <dictionary file> -p <password file>')
  parser.print_help()
  parser.add_option('-d', dest='dFile', type='string', help='specify path to dictionary file')
  parser.add_option('-p', dest='pwdFile', type='string', help='specify path to password file')
  (options,args) = parser.parse_args()

  dFile   = options.dFile
  pwdFile = options.pwdFile

  if (dFile == None) | (pwdFile == None):
        print(parser.usage)
        exit(0)
```
Our two main arguments will be the dictionary file and the password file containing the list of passwords we are trying to crack.

# Read the contents of the password file

```python
passFile = open(pwdFile)
for line in passFile.readlines():
    if ":" in line:
        user = line.split(':')[0]
        cryptPass = line.split(':')[1].strip(' ')
        print("[*] Cracking Password For:", user)
        time.sleep(1)
        testPass(cryptPass, dFile)
```

Using the built-in open() function, we create a file object, whose contents we can later read line by line.

For each line in the file object, we want to grab the password hash, so we'll only be grabbing part of each line (this makes more sense when you look at the format of UNIX password files).

Once we have the hash, we'll pass it into our testPass function, compares the hash against the hash of every word in our dictionary file.

## Test individual passwords against the dictionary file

```python
def testPass(cryptPass, dictionary):
    salt = cryptPass[0:2]
    dictFile = open(dictionary)
    for line in dictFile.readlines():
        word = line.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        # print('\t', word, ":", cryptWord, ">>>>>>", cryptPass) # DEBUG MODE to see what is being tested
        if cryptWord == cryptPass:
            print("[+] Found Password: " +word+"\n")
            return

    print("[-] Password Not Found. \n")
    return
```

This function will take an individual password and a dictionary file (read from the command line) and compare their hashes.

Just like we did with the password file, we create a file object for the dictionary file in order to hash each word. I realize that this is definitely not the most efficient process as I am creating a new file object every time I call this method. However, since this demo is simple, I'll leave it as is (don't judge).

Using basic conditional logic, we check for a match, otherwise we compare the has of the next work in the dictionary file.

```python
if __name__ == "__main__":
    main()
```

## Test Files

dictionary.txt
```python
apple
ball
cap
dog
egg
frog
golf
```

password.txt
```
user1: BXx6BeQ4xHcrI: superSecurePassword
user2: LXqkNpMH/Nt2s: 29: frog
n00b: oQh30/juuXNCo: 156: cap

```


## Output
```bash
$ python3 crypt_test.py -d dictionary.txt -p passwords.txt

Usage: usage crypt_test.py -d <dictionary file> -p <password file>

Options:
  -h, --help  show this help message and exit


[*] Cracking Password For: user1
[-] Password Not Found.

[*] Cracking Password For: user2
[+] Found Password: frog

[*] Cracking Password For: n00b
[+] Found Password: cap

```
