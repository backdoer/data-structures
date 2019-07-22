
from operator import itemgetter
from itertools import groupby
from solution import Solution, Class_Info, Overall_Solution
from Availability import Availability
from random import shuffle

MUTATION_PERCENTAGE = .05
CROSSOVER_PERCENTAGE = .8
ELITISM_PERCENTAGE = .05
NUMBER_OF_SOLUTIONS = 200



if __name__ == '__main__':
	solutions = []


	with open('classes.csv', 'r') as classes:
		overall_solutions = []
		
		classes = list(classes)
		for iteration in range(NUMBER_OF_SOLUTIONS):
			## randomize what order the classes are iterated to increase entropy
			shuffle(classes[1:])

			## create an availability object to keep track of all room availability
			avail = Availability()
			o_solution = Overall_Solution(avail)

			for i, class_info in enumerate(classes):
				if i != 0:
					class_info = class_info.strip().split(',')
					sections = int(class_info[6])

					## loop through number of sections and create a class for each
					for section in range(sections):	
						new_class = Class_Info(class_info)
						solution = Solution(new_class, avail)

						# add the inidividual solution to the overall solution
						o_solution.add_solution(solution)

			overall_solutions.append(o_solution)


	for sol in overall_solutions:
		print(sol.getFitness())
		
	# ## mutate a portion of the population
	# o_solution.mutate()

	# ## the total fitness score of this generation
	# print(o_solution.getFitness())


