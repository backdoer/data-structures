# Assignment: TNRB Classrooms

As the room scheduler for the Tanner building, you have been asked to schedule rooms and times for next semester's business management courses.  Your constraints are as follows:

* Two courses cannot be scheduled in the same room at the same time.
* Each course should be scheduled for its room at the same times each day it meets.
* Match the room size as close as possible to the number of students in each course.
* Rooms can only be used from 8am-5pm each day.
* Courses can only start on the hour or half-hour.
* When calculating free time, add 0.25 hours to the time of each course for students to move.
* Schedule courses during their preferred times of the day whenever possible.
* If you cannot find times for all courses in the building, minimize the total number of students who must leave the building for classrooms.
* Minimize the overall number of rooms used.
* Maximize blocks of free time for each room.

Write a genetic algorithm to find the best available overall fitness value that meets the constraints above.  Accept a solution when the successive generations plateau at a stable overall fitness value.

The classes are in `classes.csv` and the available rooms are in `rooms.csv`.

Create a "solution" object to represent an assignment of a section of a class.  This object should have the following methods:

```
get_fitness(): Calculates the fitness function for the current time slot.
crossover(other): Crosses with another solution and returns a new solution.
mutate(): Mutates the solution in some way.
```


## Run and Output

Run your program at least five times with different parameters.  Change the percentages of elite, crossover, and mutations each time.  Elite items are carried forward to the next generation and are not subject to mutations.

For example, you might run the following permutations:

1. 5% Elite items, 80% crossover, 5% mutations.
1. 5% Elite items, 40% crossover, 20% mutations.
1. 15% Elite items, 40% crossover, 10% mutations.
1. 25% Elite items, 80% crossover, 10% mutations.
1. 75% Elite items, 80% crossover, 5% mutations.

For each run, print the following to a text file called `run01.txt`, `run02.txt`, etc.:

```
Elite: 5%
Crossover: 80%
Mutations: 5%

Generation, Overall Fitness, Mean Course Fitness, Max Course Fitness, Min Course Fitness, Courses Scheduled, Courses Unscheduled
1, 400, 20, 80, 3, 93, 0
2, 405, 20, 82, 5, 93, 0
3, 409, 20, 84, 3, 93, 0
4, 426, 20, 82, 7, 93, 0
5, 400, 20, 86, 3, 93, 0
6, 400, 20, 87, 12, 93, 0
7, 400, 20, 89, 17, 93, 0
8, 400, 20, 95, 22, 93, 0

Room, Start Time, End Time, Course, Section
251, 9.0, 10.25, BUS M 450, 1
251, 10.5, 11.75, BUS M 450, 2
251, 2.0, 3.25, BUS M 450, 3
```

Sort the room times by room number and start time so it is easy to see that the rooms are assigned correctly.

## Crossovers

As a class

* How do we crossover without clashing with an existing room and time?

## Mutations

As a class

* How do we mutate without clashing with an existing room and time?

## Course Fitness Function

As a class


## Overall Fitness Function

As a class




## Submitting the Assignment

Zip your code and output files and submit on Learning Suite.