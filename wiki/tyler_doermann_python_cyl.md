# This code example will give a demonstration of list comprehensions 
# and how they can be useful in python. List comprehensions
# basically allow programmers to create a new list, based on attributes, 
# from a current iterable. This can be useful for filtering through
# lists quickly, getting a list of attributes from a list of objects,
# etc.
# This example will create a list of Person objects and then do a
# variety of list comprehensions on the initial list.

##create a person class real quick
class Person:
	def __init__(self, first_name, last_name, age, state, fav_color):
		self.first_name = first_name,
		self.last_name = last_name,
		self.age = age,
		self.state = state,
		self.fav_color = fav_color

## let's create a list of people, so we can do list comprehensions on it
people = []
for i in range(1, 100):
	p = Person('f_name_%s' %i, 'l_name_%s' %i, i, 'state_%s' % i, 'color_%s' % i)
	people.append(p)

##List comprehension #1
#Conditional List Comprehensions
##Old age list (older than 50)
#if you were to do this in the traditional way, it would look
# something like this:
old_people = []
for p in people:
	if p.age[0] > 50:
		old_people.append(p)

#instead, we can go like this:
old_people_lc = [p for p in people if p.age[0] > 50]
#The list old_people_lc only has people with an age over 50, and only took one line

##state having the number 5 in it
##traditional way:
state_5 = []
for p in people:
	if '5' in p.state[0]:
		state_5.append(p)

#list comprehension:
state_5_lc = [p for p in people if '5' in p.state[0]]
#The list state_5 only has people who have a 5 in their state attribute
#We could then filter this list even further by grabbing 
# only the people with a last_name containing a 2

#traditional:
state_5_lname_2 = []
for p in state_5_lc:
	if '2' in p.last_name[0]:
		state_5_lname_2.append(p)

#list comprehension:
state_5_lname_2_lc = [p for p in state_5 if '2' in p.last_name[0]]

##List comprehension #2
#Values List
##List of only first names
#traditional:
first_names = []
for p in people:
	first_names.append(p.first_name)

#list comprehension:
first_names_lc = [p.first_name for p in people]
#The list first_names_lc now has a list of all the first names of the
# people in the list 'people' and only took one line of code

##Next, let's only grab the last_names of the people who have a favorite color
# containing either a 5 or a 2
#traditional:
l_names = []
for p in people:
	if '2' in p.fav_color or '5' in p.fav_color:
		l_names.append(p.last_name)

#list comprehension
l_names_lc = [p.last_name for p in people if '2' in p.fav_color or '5' in p.fav_color]


##You can also create lists quickly using list comprehensions
#If you wanted a list of numbers ranging from 1 to 1000,
# instead of writing the following code:
numbers = []
for i in range(1, 1000):
	numbers.append(i)

#which takes 3 lines of code, you could do the following list comprehension
numbers_lc = [i for i in range(1, 1000)]
#which would have the same end result

#The moral of the story is:
#list comprehensions can simplify the creation of lists by shortening 
# the amount of code to only one line

