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
- Optionals. You can specify whether a variable is required or optional, which allows a variable to potentially be null.
- It uses dot-notation and the namespace system, which is similar to many other popular object-oriented languages.
- Swift is compiled to llvm bit-code at compile time.


##Cons
- Automatic Reference Counting for memory management allows the possibility of creating a strong reference cycle, where two instances of two different classes each include a reference to the other, causing them to become leaked into memory (because they are never released)
  - Swift provides the keywords `weak` and `unowned` to prevent this, but it can still occur if not designed and implemented properly (e.g. not using `weak` or `unowned`)
- New language
- Each release changes how things are done (always having to learn because it is so new)

##Memory management
Swift memory management is handled "behind the scenes."  However, there are some things that you should know.

Apple's version of automated memory management is called ARC, which stands for Automatic Reference Counting.  ARC tracks and manages your app's memory usage so you don't have too.  ARC's most basic functionality is that it only frees up memory for objects when there are *zero* strong references to them.  In order to understand more, it's important to know how object references work in Swift.

There are three types of object references:
1. Strong references
    - A strong reference protects an object from getting deallocated by ARC by increasing it's retain count by one.  A reference is strong by default.
1. Weak references
  - A weak reference is a pointer that doesn't increase the retain count of an object.  This means the object is not protected from being deallocated by ARC.  If you attempt to access a weak reference that has been deallocated it's value will be nil.  See [Derik Hasvold's code example](derik_hasvold_swift_example.txt) to learn how a weak reference is declared.
1. Unowned references
  - Unowned references are similar to weak references in that they do not increase an object's retained count.  However, unowned references are not optional, that is this object does not become nil when it's reference is deallocated.  However, unlike a weak reference, an error will occur if you attempt to call an unowned reference when it has been deallocated.

##Closures
Closures are self-contained blocks of functionality that can be passed around and used in your code.  Closures can captures and store references to any objects and variables from the context in which they are defined.  This is called "closing over" those constants and variables.

The closure expression syntax has the following general form:

{ (parameters) -> return type in
    statements
}

An example of a closure can be found in [Derik Hasvold's code example](derik_hasvold_swift_example.txt)

There are ways to optimize closures to reduce syntax clutter.
These optimizations include:

  - Inferring parameter and return value types from context.
  - Implicit returns from single-expression closures.
  - Shorthand argument names. See example in [Derik Hasvold's code example](derik_hasvold_swift_example.txt)
  - Trailing closure syntax.

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

## Networking in Swift - AlamoFire

Swift makes networking (making network calls, receiving data from web services, etc...) fairly simple. However, wiring up your own networking methods in Swift is akin to attempting to wire up your own networking classes and methods in Python when the pip-package `requests` exists--you just don't do it.

AlamoFire is Swift's `requests`. Built by the people that were behind the popular Objective-C networking library, `AFNetworking`, AlamoFire is written in pure Swift, making it incredibly easy-to-read, and easy-to-use. It doesn't depend on any Objective-C from it's predecessor.

Out of the box, AlamoFire comes with the following features:

- Chainable Request / Response methods
- URL / JSON / plist parameter encoding
- Upload File / Data / Stream / MultipartFormData
- Download using Request or Resume Data
- Authentication with NSURL Credential
- HTTP Response Validation
- TLS Certificate and Public Key Pinning
- Progress Closure and NSProgress (i.e., ability to show progress of network call to user)
- cURL Debug Output
- Comprehensive Unit Test Coverage
- An insane amount of documentation and tutorials on the web, due to its popularity

AlamoFire is easy to install, allowing the developer to leverage CocoaPods (the dependency manager for iOS development, akin to `pip` for Python), Carthage (another dependency manager), or manual installation from their `git` repo.

So, unless your use-case is extremely particular, involving custom-written encoders and decoders, there's really no reason for you to re-invent the wheel when it comes to Swift networking. AlamoFire is the tried and tested way to accomplish complex, interdependent iOS apps, which communicate with one or more web services.

Check out John Turner's small tutorial on hitting the OpenWeatherMap API in Swift using AlamoFire [here](alamofire_example.md).

### AlamoFire Readings, Reviews, and Tuts

- [AlamoFire Main Page / Overview](https://github.com/Alamofire/Alamofire)
- [AlamoFire Docs](http://cocoadocs.org/docsets/Alamofire/3.4.2/)
- [AlamoFire + Swift 2.2 + iOS 9.3 App Tutorial](https://www.raywenderlich.com/121540/alamofire-tutorial-getting-started)

##Resources
- [Main Website](https://swift.org/)
- [*The Swift Programming Language*][swift_book]
- [Documentation](https://swift.org/documentation/#the-swift-programming-language)
- [Getting Started Tutorial](https://swift.org/getting-started/#using-the-lldb-debugger)
- [Strong vs. Weak References](http://krakendev.io/blog/weak-and-unowned-references-in-swift)

- [Thinking in Swift (Part 2)](https://www.accelebrate.com/blog/thinking-swift-part-ii/)
- [LLVM Language Reference Manual](http://llvm.org/docs/LangRef.html)
- [Swift Compiler Architecture](https://swift.org/compiler-stdlib/#compiler-architecture)
- [Swift Book](https://swift.org/documentation/TheSwiftProgrammingLanguage) - (Swift3).epub
- [^1]: [https://www.accelebrate.com/blog/thinking-swift-part-ii/](https://www.accelebrate.com/blog/thinking-swift-part-ii/)
