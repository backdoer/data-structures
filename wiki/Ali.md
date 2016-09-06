# Dropping and Creating Databases 

This coding example shows how python can be used to drop, create, and migrate databases in a Django/Mako environment. It takes the pain out of adjusting database structures 
while developing.

This code was used last year while creating the Colonial Heritage Foundation
website using DMP. Trevor Harmon was the mastermind this code, but I've 
adjusted it for my purposes. Credit for brilliance goes to him.

***

## Setup

This code was run in a Django-Mako-Plus environment. The database used was PostgreSQL, and the server was run on the local machine for dev. 

For this to work, django had to be initialized. 

```python
# initialize django

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'CHF.settings'
import django
django.setup()
```
The `os` module provides a portable way of using operating system dependent functionality. Using `os.environ` allows us to access environment variables within the django settings module.

```python
# import helpers

from django.db import connection
import subprocess, sys
import shutil

```
* The `subprocess` module allows you to spawn new processes
* The `sys` module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.
* The `shutil` module allows for high-level file and directory handling. 

At this point, we've imported django, a connection to the database, and modules that will allow us to create new processes and mess with our environment. 

***

## Drop Database
If you've messed with a database schema, it's necessary to drop the existing database before implementing a new structure. I did so with the following code:

```python
#empty DB (aka, drop dat bass)

cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
```
The cursor class allows Python code to execute PostgreSQL commands in a database session. The `connection.cursor()` method creates a cursor that is bound to the connection for the entire lifetime and all the commands are executed in the context of the database session wrapped by the connection. So, basically, this cursor will last the lifetime of my python script. 

My cursor that is bound to my PostgreSQL session executes the command to drop my entire database schema. I'm a free woman. 

***

## Create Database
The next obvious move is to create a new database so my new structure can be implemented. 

```python
# create DB

cursor.execute("CREATE SCHEMA PUBLIC")
```
...easy enough. I created a public schema using the same cursor class that I can then create tables in and fill with data. You get the picture. 
***

## Migrate Data
Now to handle those pesky migration problems. Django uses migrations to propagate changes made to models in database schemas. In order for data to be properly added to the database, it's necessary to delete previous database migrations I added and create new ones for my new database.

```python
# Remove the existing migrations

try:
    shutil.rmtree('./account/migrations')
except:
    pass
```
The `shutil` module contains a function `rmtree` that is used to delete an entire directory tree. Since that's what migrations is, By deleting the folder, I remove all previous migrations associated with my previous database. 

Here's the rest of the migration deletions:

```python
try:
    shutil.rmtree('./catalog/migrations')
except:
    pass

try:
    shutil.rmtree('./event/migrations')
except:
    pass

try:
    shutil.rmtree('./sales/migrations')
except:
    pass
```




























