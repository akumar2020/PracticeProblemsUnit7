def factorial(num):
	'''Takes an integer and returns its factorial'''
	if num == 0:
		return 1
	else:
		return num * factorial(num - 1)

print(factorial(0))
print(factorial(1))
print(factorial(562))