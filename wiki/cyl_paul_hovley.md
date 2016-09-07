## PYTHON EXAMPLES
##Passing objects by reference Example
this example test if Python passes and assigns objects, strings, and primitives by reference or by value, meaning that if an object is 
passed to a method, any modification done to that object inside of the method it was passed to, will
modify both the object inside the method and outside.
```python
#Pointers/References
STARTING_VALUE = "unmodified"
MODIFIED_CONST = "modified"
STARTING_PRIMITIVE = 0
MODIFIED_PRIMITIVE = 1

def test_pass_string_to_meth():
    '''tests if modifying strings in methods affects the initial string outside of method'''
    test_string = STARTING_VALUE
    modify_string(test_string)
    has_string_changed(test_string)

def test_pass_obj_to_meth():
    '''tests if modifying objects in methods affects the initial object outside of method'''
    test_dict_obj = {"key": STARTING_VALUE}
    modify_object(test_dict_obj) #pass dictionary and modify values
    has_string_changed(test_dict_obj["key"])

def test_pass_prim():
    '''tests if primitives are passed to methods by value or by reference'''
    test_prim = STARTING_PRIMITIVE
    modify_prim(test_prim)
    has_prim_changed(test_prim)
 
def test_assign_obj():
    '''tests if object assignment in python is by value or by reference'''
    test_dict_obj = {"key": STARTING_VALUE}
    test_copy_obj = test_dict_obj
    test_copy_obj["key"] = MODIFIED_CONST
    has_string_changed(test_dict_obj["key"])

def test_assign_string():
    '''tests if string assignment in python is by value or by reference'''
    test_string = STARTING_VALUE
    test_copy = test_string
    test_copy = MODIFIED_CONST
    has_string_changed(test_string)

def test_assign_prim():
    '''tests if primitive assignment in python is by value or by reference'''
    test_prim = STARTING_PRIMITIVE
    test_copy = test_prim
    test_copy = MODIFIED_PRIMITIVE
    has_prim_changed(test_prim)

def modify_object(test_dict_obj):
    test_dict_obj["key"] = MODIFIED_CONST

def modify_string(test_string):
    test_string = MODIFIED_CONST

def modify_prim(test_prim):
    test_prim = MODIFIED_PRIMITIVE

def has_string_changed(test_value):
    '''test if value of dictionary has changed from starting value'''
    print("Has value changed?")
    print(test_value!=STARTING_VALUE)

def has_prim_changed(test_primitive):
    '''test if value of primitive has changed'''
    print("Has primitive changed?")
    print(test_primitive!=STARTING_PRIMITIVE)

'''MAIN METHOD CALLS'''
print("Will value change when an object is passed to a method?")
test_pass_obj_to_meth()
print("Will value of string change when passed to a method?")
test_pass_string_to_meth()
print("Will value of primitive change when passed to a method?")
test_pass_prim()
print("Are objects assiged by reference or by value?")
test_assign_obj()
print("Are strings assigned by reference or by value?")
test_assign_string()
print("Are prims assigned by reference or by value?")
test_assign_prim()
```
Result when code is run
```
Will value change when an object is passed to a method?
Has value changed?
True
Will value of string change when passed to a method?
Has value changed?
False
Will value of primitive change when passed to a method?
Has primitive changed?
False
Are objects assiged by reference or by value?
Has value changed?
True
Are strings assigned by reference or by value?
Has value changed?
False
Are prims assigned by reference or by value?
Has primitive changed?
False
```
##Interpretation:
Objects are passed and assigned by reference
Strings are passed and assigned by value
Primitives are passed and assigned by value
#Brief Call Stack Traceback Example
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

