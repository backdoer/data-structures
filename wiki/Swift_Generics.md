#Swift Generics - Kyle Longhurst

# Generics

## Example 1

Why Generics? This is a common problem that we can solve with Generics. We are going to swap the two parameters of a function. We are going to start by swapping two Integers.

```swift
func swapTwoInts(inout a: Int, inout _ b: Int) {
    let temporaryA = a
    a = b
    b = temporaryA
}

var someInt = 3
var anotherInt = 107
swapTwoInts(&someInt, &anotherInt)
print("someInt is now \(someInt), and anotherInt is now \(anotherInt)")
// Prints "someInt is now 107, and anotherInt is now 3"
```

Without generics we are restricted to copying and pasting the functions that are essentially identical.

```swift
func swapTwoStrings(inout a: String, inout _ b: String) {
    let temporaryA = a
    a = b
    b = temporaryA
}

func swapTwoDoubles(inout a: Double, inout _ b: Double) {
    let temporaryA = a
    a = b
    b = temporaryA
}
```

Let's solve this problem with Generics!

```swift
func swapTwoValues<T>(inout a: T, inout _ b: T) {
    let temporaryA = a
    a = b
    b = temporaryA
}

var someInt2 = 3
var anotherInt2 = 107
swapTwoValues(&someInt2, &anotherInt2)
// someInt is now 107, and anotherInt is now 3

var someString = "hello"
var anotherString = "world"
swapTwoValues(&someString, &anotherString)
// someString is now "world", and anotherString is now "hello"
```

Generics makes implementing this function incredibly simple! We are allowing this function to accept any type generic type, and therefore reducing the lines of code we need to write. Sometimes it takes a little more effort so we will take another look at implementing generics to add two elements together in Example 2.

## Example 2

Next, we will move on to an example that is a little more complex. With this function we will be adding two Elements of AnyType together.

```swift
func addTwoInts(x: Int, _ y: Int) -> Int {
    return x + y
}

let intSum = addTwoInts(1, 2)
```

If we want to create a function with the same functionality but for Doubles and Strings as well (and potentially more types), we have two options. First,(1) we can copy and past the functions and change the type of the parameters to accept Doubles and Strings or (2) we can use generics.

(1) Option 1 - Copy & Paste.

```swift
func addTwoDoubles(x: Double, _ y: Double) -> Double {
    return x + y
}

let doubleSum = addTwoDoubles(1.0, 2.0)

func addTwoStrings(x: String, _ y: String) -> String {
    return x + y
}

let stringSum = addTwoStrings("Hello ", "Friends")
```

(2) Option 2 — Generics

This option involves a little more work implementing a protocol for Types that can use the '+' operator. This takes adding new types to the function down to a single line of code.

```swift
protocol Summable { func +(lhs: Self, rhs: Self) -> Self }

extension Int: Summable {}
extension Double: Summable {}
extension String: Summable {}

func addTwoElements<T: Summable>(x: T, _ y: T) -> T {
    return x + y
}

let intSumWithGenerics = addTwoElements(1, 2)
let doubleSumWithGenerics = addTwoElements(1.0, 2.0)
let stringSumWithGenerics = addTwoElements("Hello ", "Class")
```

//#References
//Check out the Apple Docs and [this tutorial by Ray Wenderlich for more details](https://www.raywenderlich.com/115960/swift-tutorial-introduction-to-generics)
