## Swift ARC Examples
Note: These examples are taken from 'The Swift Programming Language (Swift 3)' Book by Apple, Inc.
Written by Jameson Ricks


## ARC in Action
This is a simple example of how Automatic Reference Counting Works
```
class Person {
    let name: String
    init(name: String) {
        self.name = name
        print("\(name) is being initialized")
    }
    deinit {
        print("\(name) is being deinitialized")
    }
}

var reference1: Person?
var reference2: Person?
var reference3: Person?

reference1 = Person(name: "John Appleseed")
/ Prints "John Appleseed is being initialized" */

reference2 = reference1
reference3 = reference1
/* This creates two more strong references to reference1 */
```
By breaking two of these references, we remove two strong references to instance.
However, one strong reference still remains and we will not see the deinit message yet.

```
reference1 = nil
reference2 = nil
/* Does not output anything to the console! */
```

When we set the last reference to nil, all strong references are removed and the `deinit` method is called.
```
reference3 = nil
/* Prints "John Appleseed is being deinitialized” */
```

## Strong Reference cycles

### The Bad Way
The declarations below create a strong reference cycle between Person and Apartment because they both have strong references associated with each other's instance.
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
    var tenant: Person?
    deinit { print("Apartment \(unit) is being deinitialized") }
}
```
Let's assign some variables and assign them to each other.
```
var john: Person?
var unit4A: Apartment?

john = Person(name: "John Appleseed")
unit4A = Apartment(unit: "4A")

john!.apartment = unit4A
unit4A!.tenant = john
```

This code creates a strong reference cycle between both class instances.
![Strong Reference Cycle](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Art/referenceCycle02_2x.png)

If we set `john` and `unit4A` to `nil`, both of the variables strong references are removed, but the strong references between the instances are still there! This prevents the instances from being deinitialized and creates a memory leak since there is no way to reference those instances now that the variables are gone. Not good!

```
john = nil
unit4A = nil

/* Does not run any deinit method because there are still strong references
to the class instances! */
```

### A Better Way

A better way to declare the classes for Person and Apartment to prevent a strong reference cycle is to use the `weak` reference on one of the variables inside a class. In this case, we declare `tenant` as a weak reference to the `Person` class.

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
    weak var tenant: Person? /* Notice the use of the weak property here! */
    deinit { print("Apartment \(unit) is being deinitialized") }
}
```
This gives us the following relationship:
![Fixed Strong Reference Cycle](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Art/weakReference01_2x.png)

Then when we run the code from above, both of our instances are successfully deinitialized!

```
var john: Person?
var unit4A: Apartment?

john = Person(name: "John Appleseed")
unit4A = Apartment(unit: "4A")

john!.apartment = unit4A
unit4A!.tenant = john

john = nil
/* Prints "John Appleseed is being deinitialized" */

unit4A = nil
/* Prints "Apartment 4A is being deinitialized" */
```
