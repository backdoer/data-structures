# Language: Python

## Characteristics:

- High-level, meaning the syntax is more readable than lower-level languages. This whole language emphasizes readability
- Interpreted, meaning it executes directly instead of being compiled by a machine language program
- Dynamic, meaning it runs certain prep code at run-time instead of during compilation, which is what non-dynamic languages do
- Multi-paradigm, meaning you can perform various programming philosophies (OOP, functional programming, etc)
- Auto-memory management, meaning you’re life is easier
- White-space indentation, meaning it doesn’t use curly braces
- Extensible, meaning the ability to be extended or augmented

## Other Info:

- CPython is the most common implementation of Python. It is written in C. This is the source code of Python.
- Began in 1989 by Van Rossom on a Christmas break while he was looking for a fun programming project to keep him busy. [Why was Python made?](https://docs.python.org/3/faq/general.html#why-was-python-created-in-the-first-place)
- Named after Monty Python [Why is it called python?](https://docs.python.org/3/faq/general.html#why-is-it-called-python)
- It has a standard library but there have been numerous libraries created to extend functionality

## Basic Philosophy:

### The Zen of Python

- Beautiful is better than ugly
- Explicit is better than implicit
- Simple is better than complex
- Complex is better than complicated
- Readability counts

The rest of the Zen can be found if you

```
import this
```
inside a python shell

## Strengths/Advantages
- Easy to use/learn
- It's object oriented and, because simplicity is stressed, it's easy to apply OOP principles. Additionally, Python comes with many built-in object types and data structures (eg. lists, dictionaries, strings, etc.) that are extremely flexible and easy to implement
- Object-oriented nature makes it an ideal tool for scripting
- OOP is also an _option_, meaning such principles can be applied if and when constraints allow
- Highly portable, meaning that it runs on basically every major platform available today
- Large support community as seen through the number of third-party libraries (Look at [PyPi](https://pypi.python.org/pypi)) for examples with Python3)
- It's *FREE*

## Drawbacks:
- It's a high level language, so you're sacrificing efficiency for convenience and readability.
- Doing things closer to the hardware is difficult because it is high-level.  Any kernal or special threading issues will be very difficult to resolve.
- Misnamed variables won't be caught unless code is run
- when working with nested functions, accessing variables in an outer scope is not possible in Python 2. There is a workaround in Python 3 via the [nonlocal statement](https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement), but that introduces a whole other pain point of backwards non-compatibility between Python 2 and 3.
- One could also say that python’s inability to distinguish between declaration and usage of a variable is an issue. What this means is that one could instantiate a variable and later accidentally write over that same variable with a redeclaration. To distinguish between the two, it could be nice to have two keywords: “let” to declare variables as read-only, and “var” variables as normal.

Consider this example:
```
x = 42    # Error: Variable `x` undeclared

var x = 1 # OK: Declares `x` and assigns a value.
x = 42    # OK: `x` is declared and mutable.

var x = 2 # Error: Redeclaration of existing variable `x`

let y     # Error: Declaration of read-only variable `y` without value
let y = 5 # OK: Declares `y` as read-only and assigns a value.

y = 23    # Error: Variable `y` is read-only
```

## Popular Use Cases
- the Dropbox desktop client and server-side code, that supports over 400 million users, are all written in python
- Spotify developed their web API and interactive API console in python
- Google itself relies heavily on python as demonstrated through their engineering mandate, “Python where we can, C++ where we must.”
- More success stories found [here](https://www.python.org/about/success/)

## Memory Management:
- Python does not specify how memory management should be implemented. The most common implementation of Python, CPython, uses a *private heap* to store all objects. [Python Docs](https://docs.python.org/3/c-api/memory.html)

From the Python documentation:

>Memory management in Python involves a private heap containing
>all Python objects and data structures. The management of this
>private heap is ensured internally by the Python memory manager.
>The Python memory manager has different components which deal with
>various dynamic storage management aspects, like sharing,
>segmentation, preallocation or caching.

- This means that *no* actual values live on the stack, only references to the objects on the stack.

- Inside the heap, objects of different types are handled differently. So integers are treated differently than strings or dictionaries, because they have different storage requirements, etc.

- There is no way for a programmer to control the Python memory manager.

## Garbage Collection:
- Python does garbage collection for the user.
- It uses reference counting meaning that it counts the number of times the object in question is referenced by the system.  When that count becomes zero, and the object is no longer referenced by anything in the system.  It is removed.
- Garbage collection is triggered when the number of allocated memory spots minus the number of deallocated memory spots is greater than some threshold number (the default is 700)
- If the system is running out of memory, an exception will fire, and no collection will be done.
- A user can manually initiate a garbage collection cycle [Python Garbage Collection Wiki](http://www.digi.com/wiki/developer/index.php/Python_Garbage_Collection)
```python
         import gc
         gc.collect()
```

Two great approaches for deciding when to manually kick off garbage collection are time-based and event-based. They are exactly as they suggest they would be; time-based kicks off on pre-determined time interval, event-based listens for certain events throughout the script to kick off the garbage collection. A great example to see manual collection at work is:

```python
import sys, gc

def make_cycle():
    l = { }
    l[0] = l

def main():
    collected = gc.collect()
    print "Garbage collector: collected %d objects." % (collected)
    print "Creating cycles..."
    for i in range(10):
        make_cycle()
    collected = gc.collect()
    print "Garbage collector: collected %d objects." % (collected)

if __name__ == "__main__":
    ret = main()
    sys.exit(ret)
```

## Code Examples

[Derek Brimley](derek_brimley_python_cyl.md)
[Dustin Belliston](dustin_belliston_python_cyl.md)
[Matt Rider](matt_rider_python_cyl.md)
