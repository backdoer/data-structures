#Swift Example - Nate Johnson

```Swift
let a = 3
let b = 4
let c = a + b
print(c)
```

The above code was saved in the file *onion.swift* and an OS X executable was created from the Swift code. Details of how to do this can be found [here](https://www.accelebrate.com/blog/thinking-swift-part-ii/).

This example will follow the addition operation of the code through the stages of the Swift compiler until it gets totally transformed into machine code.

```Swift
let c = a + b
```

## Swift Abstract Syntax Tree (AST)

```
swiftc –dump-ast onion.swift
```
The above terminal command outputs the AST for the Swift code. Below is the line of output corresponding to the addition operation.
```
(declref_expr type='(Int, Int) -> Int' location=onion.swift:4:11 range=[onion.swift:4:11 - line:4:11] decl=Swift.(file).+ specialized=no)
```

In a more readable format:

```
(declref_expr type='(Int, Int) -> Int'
  location=onion.swift:4:11
  range=[onion.swift:4:11 - line:4:11]
  decl=Swift.(file).+
  specialized=no
)
```
It's simply an expression that takes two integers as parameters and returns an integer.


## Swift Intermediate Language (SIL)

```
swiftc –emit-sil onion.swift
```

The above terminal command outputs the SIL for the Swift code. Below is the line of output corresponding to the addition operation.

```
%28 = builtin "sadd_with_overflow_Int64"(%25 : $Builtin.Int64, %26 : $Builtin.Int64, %27 : $Builtin.Int1) : $(Builtin.Int64, Builtin.Int1)
```

The operation is being performed through the *builtin* function "sadd_with_overflow_Int64". "Builtin functions are special since they are available only to the Swift standard library and typically map directly to LLVM IR instructions."[^1]

## LLVM Intermediate Representation (IR)

LLVM is the full name of the optimizer.

```
swiftc –emit-ir onion.swift
```

The above terminal command outputs the LLVM IR for the Swift code. Below is the line of output corresponding to the addition operation.

```
%9 = call { i64, i1 } @llvm.sadd.with.overflow.i64(i64 %7, i64 %8)
```

The operation is now transformed into a call to the llvm.sadd.with.overflow.i64 instruction.

## Assembly Code

```
swiftc –emit-assembly onion.swift
```

The above terminal command outputs the assembly which will generate the machine code. The source code for the addition operation does translate into the ```addq``` instruction.

[^1]: [https://www.accelebrate.com/blog/thinking-swift-part-ii/](https://www.accelebrate.com/blog/thinking-swift-part-ii/)
