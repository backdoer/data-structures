import csv
from array import Array

f = open('output.txt', 'w')

with open('data.csv', 'r') as csvfile:

	for i, row in enumerate(csv.reader(csvfile)):
		command = row[0]
		if command == 'DEBUG':
			print_value = a.debug_print()
		else:
			param1 = row[1] if len(row) > 1 else ''
			param2 = row[2] if len(row) > 2 else ''
			print_value = '%s,%s' %(param1, param2)
		f.write('%i:%s,%s \n' % (i, command, print_value))
		try:
			if command == 'CREATE':
				a = Array()
			elif command == 'ADD':
				a.add(param1)
			elif command == 'SET':
				a.set(int(param1), param2)
			elif command == 'GET':
				f.write('%s \n' % a.get(int(param1)))
			elif command == 'DELETE':
				a.delete(int(param1))
			elif command == 'INSERT':
				a.insert(int(param1), param2)
			elif command == 'SWAP':
				a.swap(int(param1), int(param2))
			
		except Exception as e:
			f.write('Error: %s \n' % e)

		
