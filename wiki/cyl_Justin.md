## Variable References in PHP ##
Author:
* Justin Jamison

In PHP, references are a way to refer to a value in memory under more than one variable. The actual value is the same for both variables, but can be referenced by both of them.

The PHP Documentation says that references are not the same as pointers in C. However, the essence of what the documentation is saying is that references are not actual memory addresses in PHP - they are aliases that point to a value in the Symbol Table.

[This site](http://code.stephenmorley.org/php/references-tutorial/) describes what PHP references are in a very simple manner.

Basically, in it's internal system, PHP stores variable references in a data structure known as the `_zval_struct`. This structure stores the value of the variable, its type, and a count of references made to that variable. This counter is called the `refcount`. When a new variable is created, the `refcount` is incremented, and the variable is added to the Symbol Table:

```php
$a = 'some value';
```

The Symbol Table is a table of mappings of the variable name and the value of that variable. It also contains the `zval` for that variable. When a variable is assigned by reference, it points to the same `zval` as another variable.

```php
$a = 12;
$b =& $a;
```

When the variable is unset, PHP removes the reference from the Symbol Table. However, the value is only removed (by garbage collection) if there are no more references to the variable.

```php
unset($example);
```

When you pass a variable to a function by reference, all the other variables that have that same reference will also have their values changed. This example demonstrates the difference between passing a value by reference, and passing it by value:

```php
// This function receives the zval, rather than the value itself!
function reference(&$var) { 
	echo "<p>" . $var . "</p>"; 
}

// This function adds using the value of the variable.
function value_add($var) { 
	$var++;
}

// This function adds by retrieving the value of the variable indicated by the zval indicated by $var.
function ref_add(&$var) { 
	$var++;
}

$a = 12;
$b =& $a; // Defining $b as pointing to the value "12" in memory - same value as $a! Both variables point to the same memory object - they have the same zval. PHP will treat both variables exactly the same!

reference($a); // Returns "12".
reference($b); // Returns "12".

value_add($b); // This will change the variable $var that is local to the function, but will not change $b! Only the value "12" was passed to the function.
value_add($a); // This will change the variable $var that is local to the function, but will not change $a! Only the value "12" was passed to the function.

echo "<p>" . $b . "</p>"; // Thus, this is still 12.
echo "<p>" . $a . "</p>"; // Also still 12.

ref_add($b); // This will add 1 to the value that $b is pointing to. Since we are passing in the reference to the value "12" (rather than the actual value "12"), the function will also change the value for all other variables that point to that value. Since $a is pointing to that same value, $a will also change to 13!

echo "<p>" . $b . "</p>"; // 13
echo "<p>" . $a . "</p>"; // 13
```

More coming soon!