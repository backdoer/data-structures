# Swift
![Alt text](https://developer.apple.com/swift/images/swift-og.png)

##Code Examples
- [Swift Basics](swift_basics.md)
  - TJ Murphy's Code Example
- [Swift Compiler](Swift_Nate_Johnson.md) (Nate Johnson)

##History
Development began in July 2010 by Chris Lattner. The 2014 Apple Worldwide Developers Conference (WWDC) application was the first app written in Swift. At that WWDC a beta version of swift was released to registered Apple developers. Along with the language *The Swift Programming Language* was also released and is available on the iBooks store and the official website. It is very easy to access and read. It explains all the fundamentals of the language.

Release History:
- beta: June 2014
- 1.0: September 9, 2014
- 1.1: October 22, 2014
- 1.2: April 8, 2014
- 2.0: September 21, 2015
- 3.0: Late 2016

##Use Cases
- Develop iOS, OS X, watchOS, tvOS, and Linux applications
- [Google is said to be considering Swift as a 'first class' language for Android](http://thenextweb.com/dd/2016/04/07/google-facebook-uber-swift/)

##Popularity
- Swift won first place for *Most Loved Programming Language* in the Stack Overflow Developer Survey 2015 and second place in 2016. [first place](https://stackoverflow.com/research/developer-survey-2015#tech-super) [second place](https://stackoverflow.com/research/developer-survey-2016#technology-most-loved-dreaded-and-wanted)
- Ranked 14th most popular language in the [TIOBE index](http://www.tiobe.com/tiobe-index//)


##Pros
- Uses the same runtime as Objective-C
  - Swift and Objective-C can be used in the same program
  - By extension, C and C++ can be used also
- Protocol-oriented Programming
  - supports categories, or methods added to extant classes at runtime
  - Swift can also add new properties, types and enums to extant instances
- Uses Automatic Reference Counting (ARC) to manage memory (has related con)
- This fall an iPad pro app called Playgrounds will be released to learn how to program in Swift
- A key element of the Swift system is its ability to be cleanly debugged and run within the development environment, using a read–eval–print loop (REPL), giving it interactive properties more in common with the scripting abilities of Python than traditional system programming languages.
- Xcode IDE is very developed and grew along side Swift
- Xcode also comes with a simulator for Apple devices
- Easy to learn
- Lots of free documentation
- iOS development is rising and one of the highest paid skills
- Type Safe language: It helps you avoid using the wrong type in certain situations (e.g. passing a String when an Int is expected)
  - Swift performs *type checks* when compiling and flags them as errors so they can be fixed even before releasing an app or an update to an app
- Swift uses type inference if a type is not declared


##Cons
- Automatic Reference Counting for memory management allows the possibility of creating a strong reference cycle, where two instances of two different classes each include a reference to the other, causing them to become leaked into memory (because they are never released)
  - Swift provides the keywords `weak` and `unowned` to prevent this, but it can still occur if not designed and implemented properly (e.g. not using `weak` or `unowned`)
- New language
- Each release changes how things are done (always having to learn because it is so new)

## The Swift Compiler
In the process of turning source code into machine code, there are typically three stages the code goes through in order to get there. "The source code is typically turned into an intermediate form, optimized, and then transformed into machine code. Those jobs can be split up into three separate components – the frontend, the optimizer, and the backend."[^1]

source code -> frontend, optimizer, backend -> machine code

For Swift, the process looks like this:

source code -> Swift Abstract Syntax Tree (AST) -> Swift Intermediate Language (SIL) -> LLVM Intermediate Representation (LLVM IR) -> machine code

[Swift Compiler](Swift_Nate_Johnson.md) provides an example of simple code analyzed at each of the three stages mentioned above.

## Automatic Reference Counting (Memory Management)
*written by Jameson Ricks*

As mentioned above, Swift has Automatic Reference Counting (ARC) that makes memory management easy. Whenever a new instance of a class is created, ARC allocates memory for that object. When the object is no longer needed, ARC automatically frees up the memory that was being used by that object.

ARC tracks how many properties, constants, and variables are currently referring to each class instance. ARC won't deallocate an instance of something until there are no active references to that instance. Whenever a property, constant, or variable is assigned, a *strong reference* is created for that instance. The reason these references are referred to as "strong" is because these references do not allow ARC to deallocate an instance when a strong reference is present.

Additionally, you can override built in `init` and `deinit` functions to print to the console, or do other actions when a class is initialized or de-initilized by ARC.

As mentioned above, a *strong reference cycle* causes two separate classes to no be full de-initilized when the variables are no longer in use. To prevent strong reference cycles, you can use `weak` references to class instances.
For example:

```
class Person {
    let name: String
    init(name: String) { self.name = name }
    var apartment: Apartment?
    deinit { print("\(name) is being deinitialized") }
}

class Apartment {
    let unit: String
    init(unit: String) { self.unit = unit }
    weak var tenant: Person?
    deinit { print("Apartment \(unit) is being deinitialized") }
}

/* Excerpt From: Apple Inc. “The Swift Programming Language (Swift 3).” */
```

Setting the `weak` reference in Apartment prevents a strong reference cycle from being created when instantiating objects as variables that relate to each other.

Similarly, there is an `unowned` reference that does not keep a strong reference to a referring instance. However, an `unowned` reference is *always* assumed to have a value and cannot be used as an optional value (i.e., no `?` after declaring the variable).

Note: `weak` and `unowned` do not always prevent strong reference cycles from happening. There are some cases where it's useful to combine an unowned property on one class and an implicitly unwrapped optional property (indicated by a `!` at the end of it's type annotation) on the other class.

More Examples: [ARC Examples](Swift_ARC_Examples.md)


##Resources
- [Main Website](https://swift.org/)
- [*The Swift Programming Language*][swift_book]
- [Documentation](https://swift.org/documentation/#the-swift-programming-language)
- [Getting Started Tutorial](https://swift.org/getting-started/#using-the-lldb-debugger)
- [Thinking in Swift (Part 2)](https://www.accelebrate.com/blog/thinking-swift-part-ii/)
- [LLVM Language Reference Manual](http://llvm.org/docs/LangRef.html)
- [Swift Compiler Architecture](https://swift.org/compiler-stdlib/#compiler-architecture)

[swift_book]: https://swift.org/documentation/TheSwiftProgrammingLanguage(Swift3).epub

[^1]: [https://www.accelebrate.com/blog/thinking-swift-part-ii/](https://www.accelebrate.com/blog/thinking-swift-part-ii/)
