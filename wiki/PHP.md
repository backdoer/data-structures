# PHP #
This page is all about the awesome scripting language known as PHP.

PHP is a scripting language that can be used for a variety of purposes. It is commonly used in web applications (either standalone or in those build on Drupal, Wordpress, etc.) to do dynamic processing on the server side. Because PHP is a server-side language, the client (browser) cannot view the actual script that generated the output - only the output (or result) of the script is visible on the client side. However, PHP has [more use cases](https://secure.php.net/manual/en/intro-whatcando.php) than just web development.

PHP's name is a recursive acronym that stands for PHP: Hypertext Processor.

If you have anything you would like to add to this tutorial about PHP, feel free to do so!

## Variable References in PHP ##

* Author: Justin Jamison
* [File](cyl_Justin.md)

In PHP, references are a way to refer to a value in memory under more than one variable. The actual value is the same for both variables, but can be referenced by both of them.

The PHP Documentation says that references are not the same as pointers in C. However, the essence of what the documentation is saying is that references are not actual memory addresses in PHP - they are aliases that point to a value in the Symbol Table.

[This site](http://code.stephenmorley.org/php/references-tutorial/) describes PHP references in a very simple manner.

### How References are Mapped to Values ###

Behind the scenes, PHP stores variable references in a data structure known as the `_zval_struct`. This structure stores the value of the variable, its type, and a count of references made to that variable. This counter is called the `refcount`. When a new variable is created, the `refcount` is incremented, and the variable is added to the Symbol Table:

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

### Returning References ###
Returning references means creating a function whose return value is the reference to a value, instead of the value itself. For example, this function returns a reference to `$test`, which is a global variable whose value gets changed every time `reference()` is called. When we call `reference()`, it increments the value of `$test` and all variables set to point to the value of `$test` reflect that new value:

```php
$test = 1;
$check = NULL;

// The "&" indicates this function should return a reference, instead of a value.
function &reference()
{
    $local =& $GLOBALS["test"]; // The variable $local in this function references global variable $test.
    $local++;
    return $local;
}

$check = &reference(); // $check is set to point to whatever &reference() returns. &reference() returns the reference to global variable $test.

echo '<p>' . $check . '</p>'; // Check is now "2".

reference();

echo '<p>' . $check . '</p>'; // Check is now "3", because calling the function reference() again incremented $test's value.
```

If we were to call `reference()` without the ampersand `&` we would instead get the following result:

```php
$check = reference(); // $check is set to whatever value reference() returns. reference() returns "2".

echo '<p>' . $check . '</p>'; // $check is now "2".

reference();

echo '<p>' . $check . '</p>'; // $check is still "2"!
```

Although `$check` was set to the value that `reference()` returns, it was not set *as a reference* to the value of `$test`. Instead, it was set to *the value* that `$test` had at that moment in time!

## References ##
 - [PHP Documentation (English)](https://secure.php.net/manual/en/)
 - [Passing Variables by Reference](http://php.net/manual/en/language.references.whatare.php)
 - [PHP references tutorial](http://code.stephenmorley.org/php/references-tutorial/)

 ## Further Reading ##
 - [Reference Mapping in PHP](http://php.net/manual/en/language.references.unset.php#82955)