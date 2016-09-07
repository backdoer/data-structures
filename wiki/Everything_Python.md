# Everything Python

A description and background of your language.  How did it start?  What is it primarily used for?  How popular is it?  What are its strengths and weaknesses?

An explanation (with examples) of how your programming language manages memory, the call/frame stack, bytecode instructions, etc.  Include information about the stack, heap, pointers and/or references, and garbage collection.

## History/Background

Food For Thought: There are some individuals in our class who are older than Python? It’s interesting to realize that while Python has become the most popular introductory teaching language at universities within the United States (and fourth in overall popularity behind timeless classics such as Java, C, and C++), Python is still relatively young at ~27 years. To illustrate python’s popularity, the Dropbox desktop client and server-side code, that supports over 400 million users, are all written in python. Spotify developed their web API and interactive API console in python. Google itself relies heavily on python as demonstrated through their engineering mandate, “Python where we can, C++ where we must.”

So how did it all start? In the early 1980’s, Guido van Rossum was working with ABC, a scripting language, and felt there was room to incorporate access to the Amoeba operating system (an operating system for networks of computers that would present the network to the user as if it were a single machine). By December 1989, Python was born. Python is an object-oriented programming language capable of interfacing with many libraries, system calls, and is extensible for applications needing a programming interface. Huge benefit of python that makes it so readily adopted is the fairly intuitive and readable syntax. To illustrate here is the simplest of examples to write “Hello World” in Java vs Python:

**JAVA**
```java
public class Main {
  public static void main(String[] args) {
     System.out.println("hello world");
   }
}
```

**PYTHON**
```python
print(‘hello world’)
```

However there are significant drawbacks to Python, as there are with each language. One that is more of an issue for some than others, but Python can be really slow when trying to do performance intensive routines. Another drawback is when working with nested functions, accessing variables in an outer scope is not possible in Python 2. There is a workaround in Python 3 via the [nonlocal statement](https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement), but that introduces a whole other pain point of backwards non-compatibility between Python 2 and 3. One could also say that python’s inability to distinguish between declaration and usage of a variable is an issue. What this means is that one could instantiate a variable and later accidentally write over that same variable with a redeclaration. To distinguish between the two, it could be nice to have two keywords: “let” to declare variables as read-only, and “var” variables as normal.

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

## Primary Use Cases

<insert content here?>

## Coded Examples

**Garbage Collection:**
In python there are two means by which memory is allocated: reference counting and garbage collection. Prior to version 2.0, Python’s interpreter was only capable of reference counting. Reference counting worked by counting how often an object was referenced by other objects in the system. Any time those references were removed the overall reference count for that object was decremented. This way at any point an object could be removed from memory when it no longer is being referred. Although extremely efficient in what it does, it fails to account for reference cycles (where an object refers to itself):

```python
def make_cycle():
    l = [ ]
    l.append(l)
 
make_cycle()
```

Unlike reference counting that is automatically computed, garbage collection is a scheduled activity. For instance, garbage collection can be triggered when certain object thresholds are hit, and monitored via:

```python
import gc
print "Garbage collection thresholds: %r" % gc.get_threshold()

# Output: Garbage collection thresholds: (700, 10, 10)
```

The above example indicates that garbage collections will run when the net total objects allocated exceeds 700, garbage collection will kick off. You can kick off garbage collection manually via the collect() of the gc library. Two great approaches for deciding when to manually kick off garbage collection are time-based and event-based. They are exactly as they suggest they would be. A great example to see manual collection at work is:

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


################## ByteCode Instructions #############
In Python, you can easily disassemble each line to show the bytecode instructions behind the scenes.
Using the command dis.dis(some_object), you are able to see the disassembly, or the source codeand instructions used to execute the commands written, for that object. 

  1          0 LOAD_CONST               0 (0)                                  
             3 LOAD_CONST               1 (('urlopen', 'Request', 'URLError')) 
             6 IMPORT_NAME              0 (urllib.request)                     
             9 IMPORT_FROM              1 (urlopen)                            
             12 STORE_NAME               1 (urlopen)                            
             15 IMPORT_FROM              2 (Request)                            
             18 STORE_NAME               2 (Request)                            
             21 IMPORT_FROM              3 (URLError)                          
             24 STORE_NAME               3 (URLError)                          
             27 POP_TOP        


This is the disassembly for the first line of my code example. I used

```
 python -m program_file.py 
```

 to output this disassembly. My first line of code is:

```
from urllib.request import urlopen, Request, URLError
```

It takes 9 commands to make this one line of code happen. To interpret the output, the number on the far left signifies the line number in the source code from which the byte code was compiled. The numbers to the right of that are the offsets of the instructions within the bytecode, which helps tell you the memory location of the data being handled by that command. Next to those numbers are found the names of the bytes, or the instruction to be used. The fourth column to the right represents the arguments used in the instruction, and is actually just a number which represents an index into other attributes of the code object. Please see http://akaptur.com/blog/2013/11/17/introduction-to-the-python-interpreter-3/ for more information. 

######## Code Example
As seen in the other examples and explanations, Python is a versatile language and has many features included in other programming languages. One nice feature of Python is being able to easily write, read, and update CSV files. CSV files are important because in e-commerce, CSVs are used primarily for importing and exporting product, customer, and order information to and from your store (see https://support.bigcommerce.com/articles/Public/What-is-a-CSV-file-and-how-do-I-save-my-spreadsheet-as-one). 
As seen my in code example, you can also easily pull data through APIs from any place which offers an API. See [Bruce Hansen's code example](ballapi.py)



