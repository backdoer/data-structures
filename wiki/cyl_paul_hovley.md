## PYTHON EXAMPLES
##Passing values by reference Example
this example demonstrates that Python passes objects by reference, meaning that if an object is 
passed to a method, any modification done to that object inside of the method it was passed to, will
modify both the object inside the method and outside.
```python
#Pointers/References
def modify_dictionary(dictionary_ref):
    dictionary_copy = dictionary_ref #dictionary_copy is actually pointing at the memory location of dictionary_ref
    dictionary_copy["key"] = "modified"
    print "Dictionary copy inside: " 
    print dictionary_copy

dictionary_ref = {"key": "start"}
print "Dictionary ref start value" 
print dictionary_ref

modify_dictionary(dictionary_ref)
print "Dictionary ref after: "
print dictionary_ref

Dictionary ref start value
{'key': 'start'}
Dictionary copy inside: 
{'key': 'modified'}
Dictionary ref after: 
{'key': 'modified'} 
```
#Brief Call Stack Example
This brief example demonstrates what the call stack will look like after a number of methods
are called in python
```python
import traceback
def first_method():
    try:
        second_method()
    except:
        traceback.print_exc()

def second_method():
    raise_exception_method()

def raise_exception_method():
    raise Exception('Exceptional Exception')

first_method()

Traceback (most recent call last):
  File "./call_stack.py", line 19, in first_method
    second_method()
  File "./call_stack.py", line 25, in second_method
    raise_exception_method()
  File "./call_stack.py", line 28, in raise_exception_method
    raise Exception('Exceptional Exception')
Exception: Exceptional Exception
```
Python behaves in a similar manner to most high-level languages in that it provides a trace for the methods in the order the were pushed onto the stack.  

