from Availability import WEEKDAYS, group, WALKING_TIME, TIME_CHUNKS
import datetime
import math
from random import randint

BASE_TIME = datetime.datetime(1, 1, 1,8)
HALF_HOUR = 30
NOON = datetime.time(1, 1, 1, 12)
TOTAL_FREE_TIME_BLOCKS = 2880
TOTAL_STUDENTS = 6277
TOTAL_ROOMS = 32
TOTAL_SOLUTIONS = 93

class Overall_Solution(object):
	def __init__(self, avail):
		self.avail = avail
		self.solutions = []
		self.total_ind_fitness = 0

	def add_solution(self, solution):
		self.solutions.append(solution)
		self.total_ind_fitness += solution.getFitness()

	def getFitness(self):
		return self._get_free_time_score() * .2 + self._get_avg_ind() * .6 + self._get_students_outside_tnrb_score() * .2 + self._get_unused_rooms_score() * .2

	def _get_avg_ind(self):
		return self.total_ind_fitness / TOTAL_SOLUTIONS

	def _get_free_time_score(self):
		total = 0
		for day in self.avail.codes.keys():
			for room in self.avail.codes[day]:
				consecs = list(group(self.avail.codes[day][room]))
				greatest_consec = 0
				consecs = [consec[1] - consec[0] for consec in consecs]
				greatest_consec = max(consecs)
				total += greatest_consec
		return (total * 100) / TOTAL_FREE_TIME_BLOCKS

	def _get_students_outside_tnrb_score(self):
		total_students = 0
		for solution in self.solutions:
			if not solution.solution:
				total_students += solution.class_info.num_students
		return (total_students * 100) / TOTAL_STUDENTS

	def _get_unused_rooms_score(self):
		##initiate a new list of room numbers
		unused_rooms = list(self.avail.rooms.keys())
		for solution in self.solutions:
			if solution.solution:
				room_num = solution.room.room_num
				if room_num in unused_rooms:
					unused_rooms.remove(room_num)
		return len(unused_rooms) * 100 / TOTAL_ROOMS


	def crossover(self, other):
		pass

	def mutate(self):	
		## randomly select 5 class assignments to mutate
		for x in range(5):
			solution = self.solutions[randint(0, len(self.solutions)-1)]
			## if there is a solution, put back the values it took from the availability object
			if solution.solution:
				## add the time values back to avail object before randomly re-assining an available spot
				for day in solution.class_info.days:
					top_index = solution.start_time_index + math.ceil((solution.class_info.length + WALKING_TIME)/TIME_CHUNKS)
					for block in range(solution.start_time_index, top_index):
						solution.avail.codes[day][solution.room.room_num].append(block)

			## randomly assign a new available spot
			solution.__init__(solution.class_info, solution.avail)

class Solution(object):
	def __init__(self, class_info, avail):
		self.avail = avail
		self.class_info = class_info
		self.solution = self.avail.getFreeSlot(self.class_info.length, self.class_info.days, self.class_info.num_students)
		if self.solution:
			## Room object
			self.room = self.solution[0]

			## Start time index 
			self.start_time_index = self.solution[1]

			self.start_time = BASE_TIME + datetime.timedelta(minutes=(HALF_HOUR * self.start_time_index - 1))
			self.end_time = (self.start_time + datetime.timedelta(hours=self.class_info.length)).time()

			## Convert to time after timedelta
			self.start_time = self.start_time.time()
		

	def __str__(self):
		if self.room:
			return '%s, with %s students, will be held on %s for %s hours in room %s from %s to %s' % (self.class_info.class_name, self.class_info.num_students, self.class_info.days, self.class_info.length, self.room.room_num, self.start_time, self.end_time)
		else:
			return 'No solution has been found yet'

	def getFitness(self):
		if self.solution:
			return self.get_capacity_value() + self.get_pref_type_value() + self.get_pref_time_value()
		else:
			return 0

	def get_capacity_value(self):
		diff = self.room.capacity - self.class_info.num_students
		if diff < 6:
			value = 50
		elif diff < 11:
			value = 40
		elif diff < 16:
			value = 30
		elif diff < 21:
			value = 20
		elif diff < 26:
			value = 10
		else:
			value = 0
		return value

	def get_pref_type_value(self):
		if self.class_info.preferred_type == self.room.room_type:
			value = 25
		else:
			value = 0
		return value

	def get_pref_time_value(self):
		value = 0
		if (self.start_time < NOON and self.class_info.preferred_time == 'Morning') or (self.start_time > NOON and self.class_info.preferred_time == 'Afternoon'):
			value = 25
		elif self.start_time <= NOON <= self.end_time:
			value = 15
		return value




class Class_Info(object):

	def __init__(self, line):
		self.class_name = line[0]
		self.days = self._convert_to_days(line[1:6])
		self.length = float(line[7])
		self.preferred_time = line[8]
		self.preferred_type = line[9]
		self.num_students = int(line[10])

	def _convert_to_days(self, days):
		appended_days = []
		for i, val in enumerate(days):
			if val:
				appended_days.append(WEEKDAYS[i])
		return appended_days






