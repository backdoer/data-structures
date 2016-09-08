##Optionals code examples


##Basic function we will use in this example

func findStockCode(company: String) -> String? {
   if (company == "Apple") {
      return "AAPL"
   } else if (company == "Google") {
      return "GOOG"
   }

   return nil
}

##Optionals used here because it is unknown if a value will be returned from the function findStockCode
##This will fail at runtime because message cannot concatenate text with a nil value
var stockCode:String? = findStockCode("Facebook")
let text = "Stock Code - "
let message = text + stockCode  // compile-time error
println(message)

##Unwrapping optionals

##Here we test to see if a value exists before we do something with the message
##The variable stockCode can then be unwrapped using the ! symbol
var stockCode:String? = findStockCode("Facebook")
let text = "Stock Code - "
if stockCode {
    let message = text + stockCode!
    println(message)
}

##Unwrapping without checking for a value first
##We tell swift that a value will be there, promising that it won't be nil however because we pass it something other than Apple or Google it will fail at runtime because stockCode will have a nil value
var stockCode:String? = findStockCode("Facebook")
let text = "Stock Code - "
let message = text + stockCode!  // runtime error

##Optional Binding
##if let or if var are the two keywords of optional binding. In plain English, the code says “If stockCode contains a value, unwrap it, set its value to tempStockCode and execute the conditional block. Otherwise, just skip it the block”. As the tempStockCode is a new constant, you no longer need to use the ! suffix to access its value
var stockCode:String? = findStockCode("Facebook")
let text = "Stock Code - "
if let tempStockCode = stockCode {
    let message = text + tempStockCode
    println(message)
}

##Further simplify Code
let text = "Stock Code - "
if var stockCode = findStockCode("Apple") {
    let message = text + stockCode
    println(message)
}



