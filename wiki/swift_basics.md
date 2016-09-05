#The Basics of Swift
The goal of this example is to show how to do the very basics of Swift. For example, variables, constants, functions, etc.

##variables
You can set a variable without specifying a type:
`var example = 45`
This will set the type to be an Int

You can also provide a type annotation as follows:
`var exampleString: String = "Hi There!"`
This will strongly type that variable.

You can also declare multiple variables at once:
`var example1 = 'A', example2 = 'B', example3 = 'C'`
or
`var example1, example2, example3: String`

You can specify a variable as optional as follows:
`var surveyAnswer: String?`
surveyAnswer is automatically set to nil

An optional variable can also be assigned to a null value after having a value previously:
`var serverResponseCode: Int? = 404`
serverResponseCode contains an actual Int value of 404
`serverResponseCode = nil`
serverResponseCode now contains no value

In order to access the value of an optional variable, you must unwrap it, but ONLY if it actually has a value and is not nil:
`if convertedNumber != nil {
    print("convertedNumber has an integer value of \(convertedNumber!).")
}`

##Constants
Constants have all the same capabilities of variables, except they cannot be changed once set. Here is how you set a constant:
`let exampleConstant = 45`

##Comments
Swift allows for single line comments:
`// This is a single line comment`
and
`/*This is a multiple
line comment
that covers multiple
lines*/`
or
`/*This is the first line
  /*This is a nested multiple
  line comment*/
And this is the last line of the original comment*/`

##Operators
###Assignment operator (`=`)
` var equalSign = 42`

###Arithmetic Operators
- Addition (+)
  - `var add = 1 + 2`
- Subtraction (-)
  - `var subtract = 2 - 1`
- Multiplication (\*)
  - `var multiply = 3 * 2`
- Division (/)
  - `var divide = 6 / 2`
- Remainder (%)
  - `var remainder = 10 % 3`
  - Returns `1` because 3 goes into 10 3 times with a REMAINDER of 1

###Comparison Operators
- Equal to (==)
  - `1 == 2 // false because 1 does not equal 2`
- Not Equal to (!=)
  - `1 != 2 // true because 1 does not equal 2`
- Less Than (<)
  - `4 < 4 // false because 4 is not less than 4`
- Greater Than (>)
  - `5 > 1 // true because 5 is greater than 1`
- Less Than or Equal to (<=)
  - `4 <= 4 // true because 4 is equal to 4 (can be less than OR equal to)`
- Greater Than or Equal to (>=)
  - `10 >= 9 // true because 10 is great than 9 (can be greater than OR equal to)`

###Ternary Conditional Operator
The ternary conditional operator is shorthand for a if, else statement and uses the `someBool ? a : b` format
- `var someBool = true
  var a = 1
  var b = 0
  var newVar = someBool ? a: b // sets newVar to 1 because someBool is true and so it returns a, which is 1`

###Range Operators
There are two range operators, *closed range* operator and *half-open range* operator:
- Closed Range Operator `1...10` includes the numbers between 1 through 10 and includes 1 and 10 as well
  - `for counter in 2...6 {
      print("/(counter) times 3 is /(counter * 3)")
    }

    // 2 times 3 is 6
    // 3 times 3 is 9
    // 4 times 3 is 12
    // 5 times 3 is 15
    // 6 times 3 is 18`
- Half-open Range Operator `3..<5` includes 3 through 4 and excludes 5
  - `for counter in 3..<5 {
      print("/(counter)")
    }

    // 3
    // 4`

###Logical Operators
- Logical NOT (!a)
  - `if !someBool {
      print("Now you see me!")
    }

    // Now you see me!`
- Logical AND (a && b)
  - `if a && b { // a is true, b is false
      print("Now you see me!")
    }

    // Nothing will print in this example because not both a and b are true`
- Logical OR (a || b)
  - `if a || b { // a is true, b is false
      print("Now you see me!")
    }

    // Now you see me! will print because either a or b must be true and a is true`
