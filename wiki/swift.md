# Swift
![Alt text](https://developer.apple.com/swift/images/swift-og.png)

##Code Examples
- [Swift Basics](swift_basics.md)
  - TJ Murphy's Code Example
- [Swift Compiler](Swift_Nate_Johnson.md) (Nate Johnson)
- [Structs vs Classes with Tuples](Swift-StructsVsClassesWithTuples.md)
  - Michael Perry Code Example

##History
Development began in July 2010 by Chris Lattner. The 2014 Apple Worldwide Developers Conference (WWDC) application was the first app written in Swift. At that WWDC a beta version of swift was released to registered Apple developers. Along with the language *The Swift Programming Language* was also released and is available on the iBooks store and the official website. It is very easy to access and read. It explains all the fundamentals of the language.
Recently the language has become open source. Apple claims that Swift is much faster than Apples traditional language of choice, Objective-C.

Release History:
- beta: June 2014
- 1.0: September 9, 2014
- 1.1: October 22, 2014
- 1.2: April 8, 2014
- 2.0: September 21, 2015
- 3.0: Late 2016

##Use Cases
Swift is currently used primarily for Apple applications, such as in WatchOS, OSX, iOS, tvOS, and everything else Apple. Now that it has been open sourced for some time and is gaining some traction outside of Apple. There is a company called PerfectlySoft Inc. who developed a server-side architecture using Swift. The main goal of this architecture is to provide back-end services to iOS and OSX developers so that they can build an entire solution in Swift.

- Develop iOS, OS X, watchOS, tvOS, and Linux applications
- [Google is said to be considering Swift as a 'first class' language for Android](http://thenextweb.com/dd/2016/04/07/google-facebook-uber-swift/)

##Popularity
- Swift won first place for *Most Loved Programming Language* in the Stack Overflow Developer Survey 2015 and second place in 2016. [first place](https://stackoverflow.com/research/developer-survey-2015#tech-super) [second place](https://stackoverflow.com/research/developer-survey-2016#technology-most-loved-dreaded-and-wanted)
- Ranked 14th most popular language in the [TIOBE index](http://www.tiobe.com/tiobe-index//)
Swift is become popular very quickly given how short of a time the language has existed. With only two years under its belt, Swift already has a strong community of developers online and it is often fairly easy to find solutions and help on stack overflow. Something that helps in making Swift usable is the fact that Apple has made it easy to add Swift to an Objective-C project and visa-versa. Swift also accesses the same base libraries as Objective-C and has most of the same functionality. This is a strong benifit for Swift becasue there is a large community with many answers online that are in Objective-C and which can easily be translated into Swift by a developer. Thus, a lot of the existing Objective-C help and documentation can be used to help solve problems in Swift.

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

Apple built Swift from the ground up, using a lot of smart people and a clear and definite purpose. Swift combines all of the conviences of modern scripting languages, such as dynamic typing, with the efficiency of more traditional lower level languages such as C# and Java. By so doing, Swift is easy to use, learn, write, and it is very robust and fast. Here are a few listed specific reasons why Swift is awesome:
- Dynamic types - Swift uses dynamic type but is safe an efficient. It is safe an efficient for a couple different reasons. (1) Swift requires you to explicitly state your intent with a variable and speicify whehter it is a constant using the keyword "let", or whether it is a normal variable that will change throughout runtime such as "var". (2) If the data type of a variable cannot be infered by its definition then you must explicitly state its type, this helps make the language more secure and readable.
- Optionals - Swift forces a convention that greatly assists in preventing null or nil objects during runtime. Swift accomplishes this by what Apple has called optionals. With optionals you must specify whether or not an object will be nil during runtime. This helps the developer be more aware of their code and have better coding practices. The compiler forces you to specify whether an object is nullable to help you be more aware that this object could cause problems during runtime.
- Closures - Closures are like really cool functions that you can run in Swift that do something in a very brief and implied manner. For example, you can use a closure that sorts and array of objects by some attribute in that object (such as age or date of birth). This closure is a short call end the end of the array and it will intellengently figure out on its own how to sort whatever you requested to sort (for example if it is an int or a date or some other type).
- Tuples - Tuples are just awesome. With a touple you can do all kinds of cool stuff, including having functions that return multiple values. For example, you can have a function that returns (int, String, CustomObject) or whatever else you want. This feature is great for when you have a function that can return multiple values. So if you have a function that calculates multiple values, instead of writing multiple functions that have a lot of the same code to get the different values or having so set class variables from within a function (which gets messey), you can simply encapsulate all of the return values into one function.
- Extensions - Extensions are a common feature in other languages but Swift makes it super easy. All you have to do, is use the extension keyword and then you can modify any class you want. For example, lets say you want to count the longest consecutive length of integers in a String and you want to use this feature all over your program. Well there is a simple solution, create an extension and extend the base class String and add a method to that class that counts the longest consecutive length of integers. Now with any normal string in your program, you can call this method.

##Cons
- Automatic Reference Counting for memory management allows the possibility of creating a strong reference cycle, where two instances of two different classes each include a reference to the other, causing them to become leaked into memory (because they are never released)
  - Swift provides the keywords `weak` and `unowned` to prevent this, but it can still occur if not designed and implemented properly (e.g. not using `weak` or `unowned`)
- New language
- Each release changes how things are done (always having to learn because it is so new)
- Tuples can be dangerous - Tuples are awesome but if done poorly they can get messey. They are a powerful tool that allows you to pull a lot more from a single function, but if used incorrectly you might actually complicate your code and hide certain parts of your Model that should be abstracted away from a single function.
- Dynamic types - If you are going to do dynamic types, then Swift is the way to go. But despite the beauty of Swift's approach to dynamic typing it does come at a cost in speed and efficiency.
- Garbage collection - Swift has a great garbage collector, but as in all languages that intellengently manage memory, Swift isn't going to be as efficient as an expertly developed program in C++.

##Memory management
Swift memory management is handled "behind the scenes."  However, there are some things that you should know.

Apple's version of automated memory management is called ARC, which stands for Automatic Reference Counting.  ARC tracks and manages your app's memory usage so you don't have too.  ARC's most basic functionality is that it only frees up memory for objects when there are *zero* strong references to them.  In order to understand more, it's important to know how object references work in Swift.

There are three types of object references:

1. Strong references
    - A strong reference protects an object from getting deallocated by ARC by increasing it's retain count by one.  A reference is strong by default.
1. Weak references
  - A weak reference is a pointer that doesn't increase the retain count of an object.  This means the object is not protected from being deallocated by ARC.  If you attempt to access a weak reference that has been deallocated it's value will be nil.  See [Derik Hasvold's code example](derik_hasvold_swift_example.md) to learn how a weak reference is declared.
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

## Generics
According to the Apple documentation on Swift, generics are used all throughout the Swift language. Where did the name 'generics' come from you ask? Well generics are used to allow a function or class accept any generic type. So, to not use the word generics in the definition, let me give you an example.

Lets assume you have a function that adds two Integers together. If you want to do the same thing with two Doubles or two Strings, you could:

(1) create two more almost identical function that accepts two Doubles/Strings
or (2) you could modify your first function to accept a parameter of any type. (Generics, simple)

You have been using Generics and you probably didn't even know it. In Swift, Arrays and Dictionaries are also generics. When you initialize an Array you declare the type that will be stored in that Array. That is Swift utilizing the powers of Generics.

If you want to learn more [Generic Examples](Swift_Generics.md) provides examples of some basic generic functions in Swift.

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


## Error Handling

Error handling refers to the anticipation, detection and resolution of programming applications and communication errors. Error handling is a useful practice for all programmers and should be used regularly to improve the smooth flow of a program, debugging, user experiences, etc.

Since the release of Swift 2, error handling has become much easier to implement than what it was in the previous version of Swift. The historical method for handling error is by using an NSError object passed as a pointer. When you called a method that could fail, you would pass in an empty NSError as a parameter, which would get filled up if there were a problem. This freed up the return value of the method to be the data you actually cared about. For example, loading an NSString from disk looked like this in Swift 1.2:

```
var err: NSError?
let contents = NSString(contentsOfFile: filePath, encoding: NSUTF8StringEncoding, error: &err)

if err != nil {
// uh-oh!
}  
```

In Swift 2 however, there are four ways to handle errors. You can propagate the error from a function to the code that calls that function, handle the error using a do-catch statement, handle the error as an optional value, or assert that the error will not occur.

Here is an example of error handling using [Throwing Functions](Swift_Tanner_Sawyer.md)
    -Tanner Sawyer
You can see examples of the other types of error [here](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/ErrorHandling.html)




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

##Student Examples
[Error Handling](Swift_Tanner_Sawyer.md) by Tanner Sawyer

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
