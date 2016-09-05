
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

