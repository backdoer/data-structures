from itertools import groupby
from operator import itemgetter
import math
from random import randint,shuffle

WEEKDAYS = ['M', 'T', 'W', 'TH', 'F']
WALKING_TIME = .25
TIME_CHUNKS = .5
TIME_CHUNKS_IN_DAY = 19


class Availability(object):
	def __init__(self):
		self.codes = {}
		## initialize the days
		for day in WEEKDAYS:
			self.codes[day] = {}

		self.rooms = {}

		self._convert_rooms()

	def _convert_rooms(self):

		with open('rooms.csv', 'r') as rooms:
			for room in rooms:
				values = room.split(',')
				room_num = values[0]
				if room_num != 'Room':

					self.rooms[room_num] = Room(room_num, int(values[1]), values[2])

					for day in WEEKDAYS:
						self.codes[day][room_num] = [num for num in range(1, TIME_CHUNKS_IN_DAY)]

	def getFreeSlot(self, length, days, num_students):
		##This function finds a time slot on the specified days. I saw the Days as a constraint as opposed to being part of the fitness
		## function and so I made sure that a time slot was only returned if it fit within the specified days
		self.needed_slots = math.ceil((length + WALKING_TIME)/TIME_CHUNKS)

		day1 = self.codes[days[0]]

		if len(days) > 1:
			day2 = self.codes[days[1]]
		else:
			day2 = None

		for room_num in day1.keys():
			if self.rooms[room_num].capacity > num_students:

				if day2:
					combined_avail = day1[room_num] + day2[room_num]
					##get time slots that exist for both days
					available_times = [key for key,group in groupby(sorted(combined_avail)) if len(list(group)) > 1]
				else:
					available_times = day1[room_num]

				return_slot = self._get_return_slot(available_times)

				if return_slot:
					for val in return_slot:
						
						day1[room_num].remove(val)
						
						if day2:
							day2[room_num].remove(val)
					## as soon as an open slot is found, it is returned
					return self.rooms[room_num], return_slot[0]
		##if no solution is found, return None
		return None



	def _get_return_slot(self, available_times):
		## loop through the consecutive time blocks in the duplicate time blocks
		if available_times:
			consecs = list(group(available_times))
			shuffle(consecs)
			for consec in consecs:
				# if the consecutive time block is large enough for the needed slot, then use it
				if consec[1] - consec[0] > self.needed_slots:
					##randomly selecta time block from the consecutive time block
					rand = randint(consec[0], consec[1] - self.needed_slots)
					return list(range(rand,(rand+self.needed_slots)))
		return None


def group(L):
    first = last = L[0]
    for n in L[1:]:
        if n - 1 == last: # Part of the group, bump the end
            last = n
        else: # Not part of the group, yield current group and start a new
            yield first, last
            first = last = n
    yield first, last # Yield the last group


class Room(object):
	def __init__(self, number, capacity, room_type):
		self.room_num = number
		self.capacity = capacity
		self.room_type = room_type


			






