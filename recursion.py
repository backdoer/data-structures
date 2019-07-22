##recursion

def factorial(num):
	if num == 2:
		return 2
	return factorial(num - 1) * num

fact_numbers = [5, 8, 20, 100, 999]
for num in fact_numbers:
	try:
		print(factorial(num))
	except RecursionError:
		print('recursion max reached')

    
    
