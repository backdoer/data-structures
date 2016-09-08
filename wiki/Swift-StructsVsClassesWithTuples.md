```Swift
/* 
 This is a Swift playground program used to demonstrate the difference between a struct and a class in Swift and to show how Tuples work.
 A difference between structs and classes is how they are assigned (how they behave when you use the "=" operator). When you assign a
 new variable to an existing class you are not making a copy of the object and assigning new memory for a whole new object, you are 
 simply creating a copy of the reference. Thus, if you assign a new variable to an existing object and modify that object, then you 
 modify the existing object becasue you only copied the reference, you didn't create a copy of the object in memory. With a struct, 
 when you make a new variable assignment to a previous struct you actually assign new memory for the new variable assignment. Thus,
 when you modify the new variable of a struct you don't change the value of the initial struct.
*/
import Foundation

extension NSDate {
    convenience init(dateString:String) {
        let dateStringFormatter = NSDateFormatter()
        dateStringFormatter.dateFormat = "yyyy-MM-dd"
        dateStringFormatter.locale = NSLocale(localeIdentifier: "en_US_POSIX")
        let d = dateStringFormatter.dateFromString(dateString)!
        self.init(timeInterval:0, sinceDate:d)
    }
    func yearsFrom(date: NSDate) -> Int {
        return NSCalendar.currentCalendar().components(.Year, fromDate: date, toDate: self, options: []).year
    }
    func offsetFrom(date: NSDate) -> String {
        if yearsFrom(date)   > 0 { return "\(yearsFrom(date))y"   }
        return ""
    }
}

// Person class with basic attributes
class PersonClass {
    var firstName: String!
    var lastName: String!
    var hairColor: String!
    private var age: Int!
    var birthDay: NSDate! {
        didSet {
            let dateNow = NSDate()
            age = dateNow.yearsFrom(birthDay)
        }
    }
    
    init(firstName: String, lastName: String, hairColor: String, birthDay: NSDate) {
        self.firstName = firstName
        self.lastName = lastName
        self.hairColor = hairColor
        self.birthDay = birthDay
        
        let dateNow = NSDate()
        age = dateNow.yearsFrom(birthDay)
    }
}

// Identical Person struct as class with same basic attributes
struct PersonStruct {
    var firstName: String!
    var lastName: String!
    var hairColor: String!
    private var age: Int!
    var birthDay: NSDate! {
        didSet {
            let dateNow = NSDate()
            age = dateNow.yearsFrom(birthDay)
        }
    }
    
    init(firstName: String, lastName: String, hairColor: String, birthDay: NSDate) {
        self.firstName = firstName
        self.lastName = lastName
        self.hairColor = hairColor
        self.birthDay = birthDay
        
        let dateNow = NSDate()
        age = dateNow.yearsFrom(birthDay)
    }
}

// Create instance of initial struct and class persons, note the values of the input
var michaelAsClass = PersonClass(firstName: "Michael", lastName: "Perry", hairColor: "Brown", birthDay: NSDate(dateString: "1993-06-27"))
var michaelAsStruct = PersonStruct(firstName: "Michael", lastName: "Perry", hairColor: "Brown", birthDay: NSDate(dateString: "1993-06-27"))

// This is a tuple function that outputs three values. In the function we reassign the class twice as we change values and reassign the struct once
// We then return the inital class, the initial struct, and the changed struct
func getPersonClassAndStructReassignments(initialPersonClass: PersonClass, initialPersonStruct: PersonStruct) -> (reassignedClass: PersonClass, initialPersonStruct: PersonStruct, reassignedStruct: PersonStruct) {
    // Create a new variable [reference] to the inital class object and change the values
    let personClassReference = initialPersonClass
    personClassReference.firstName = "Jim"
    personClassReference.lastName = "Love"
    personClassReference.birthDay = NSDate(dateString: "2015-02-12")
    
    // Create another reference to the previous reference we just copied and change one of the obejct values
    let jim = personClassReference
    jim.firstName = "Cutie"
    
    // Create a copy of the previous struct by using the same assignment pattern as in the previous class and change the values
    var personStructCopy = initialPersonStruct
    personStructCopy.firstName = "Jim"
    personStructCopy.lastName = "Love"
    personStructCopy.hairColor = "Blue"
    personStructCopy.birthDay = NSDate(dateString: "2015-02-12")
    
    return (initialPersonClass, initialPersonStruct, personStructCopy)
}
// Get the output from the function above
let results = getPersonClassAndStructReassignments(michaelAsClass, initialPersonStruct: michaelAsStruct)
/*
 Notice in the output that the classes reference was copied twice and changed values within each copy, and the output is whatever the last
 change to any of the variables asssigned to that reference was. This is becasue we are passing a reference to the initial object.
 
 Now notice the inital struct, all of its values remained the same. This is becasue new variable assignment creates a copy in memory.
 
 Now notice the output of the struct copy we changed the values of. All of the values of the struct copy have been reassigned by the function.
*/

print("Class Results\n")
print(results.reassignedClass.firstName)
print(results.reassignedClass.lastName)
print(results.reassignedClass.hairColor)
print(results.reassignedClass.age)
print("\nStruct Results - Initial\n")
print(results.initialPersonStruct.firstName)
print(results.initialPersonStruct.lastName)
print(results.initialPersonStruct.hairColor)
print(results.initialPersonStruct.age)
print("\nStruct Results - Output\n")
print(results.reassignedStruct.firstName)
print(results.reassignedStruct.lastName)
print(results.reassignedStruct.hairColor)
print(results.reassignedStruct.age)

```
