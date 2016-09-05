# Swift

## The Swift Compiler (Nate Johnson)

In the process of turning source code into machine code, there are typically three stages the code goes through in order to get there. "The source code is typically turned into an intermediate form, optimized, and then transformed into machine code. Those jobs can be split up into three separate components – the frontend, the optimizer, and the backend."[^1]

source code -> frontend, optimizer, backend -> machine code

For Swift, the process looks like this:

source code -> Swift Abstract Syntax Tree (AST) -> Swift Intermediate Language (SIL) -> LLVM Intermediate Representation (LLVM IR) -> machine code

[Nate_Johnson_Example](Swift_Nate_Johnson.md) provides an example of simple code analyzed at each of the three stages mentioned above.

## Resources
- [Thinking in Swift (Part 2)](https://www.accelebrate.com/blog/thinking-swift-part-ii/)
- [LLVM Language Reference Manual](http://llvm.org/docs/LangRef.html)
- [Swift Compiler Architecture](https://swift.org/compiler-stdlib/#compiler-architecture)

[^1]: [https://www.accelebrate.com/blog/thinking-swift-part-ii/](https://www.accelebrate.com/blog/thinking-swift-part-ii/)
