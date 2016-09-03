# Swift
![Alt text](https://developer.apple.com/swift/images/swift-og.png)

##Code Examples
- [Swift Basics](../swift_basics.md)

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

##Resources
- [Main Website](https://swift.org/)
- [*The Swift Programming Language*][swift_book]
- [Documentation](https://swift.org/documentation/#the-swift-programming-language)
- [Getting Started Tutorial](https://swift.org/getting-started/#using-the-lldb-debugger)

[swift_book]: https://swift.org/documentation/TheSwiftProgrammingLanguage(Swift3).epub
