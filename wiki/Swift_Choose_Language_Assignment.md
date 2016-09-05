# Swift

* A description and background of your language.  How did it start?  What is it primarily used for?  How popular is it?  What are its strengths and weaknesses?

Swift was first introduced on June 2, 2014 with the 1.0 version milestone being reached on September 9, 2014. It's development began in 2010 by Chris Lattner. It was originally a proprietary language, but later became open-source.

It is an alternative to Objective-C that has a supposedly more simple syntax and modern programming-language theory concepts. It uses dot-notation and the namespace system, which is similar to many other popular object-oriented languages. It also does not expose pointers by default. It does have some language concepts that come from functional programming.

A big strength of the language is the safety of the language. In Objective-C, entire classes of errors would occur making app crashes very common. That no longer happens reducing the crashes. Another strength has to do with its optionals. You can specify whether a variable is required or optional, which allows a variable to potentially be null.

The biggest downside is probably the fact that this is a fledgling language. Granted, Swift 3.0 was recently announced, but it's only been around officially for 2 years. This means that there is a learning curve to it, and there won't be as comprehensive support for it as there is for another language that is much more mature, like Java. Even so, it has gained a lot of popularity in it's short lifespan.

## Inner Workings
-----

 * An explanation (with examples) of how your programming language manages memory, the call/frame stack, bytecode instructions, etc.  Include information about the stack, heap, pointers and/or references, and garbage collection.

 Swift uses Automatic Reference Counting for memory management. This is nice because it used to all be manual memory management with Objective-C whereas now it is mostly automatic.

 Swift is compiled to llvm bit-code at compile time.
