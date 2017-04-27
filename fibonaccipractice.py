def fibonacci(n):
	'''Takes an index 'n' and returns the nth fibonacci number'''
	if n <= 1:
		return 1
	else:
		return (fibonacci(n - 2) + fibonacci(n - 1))

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(4))
print(fibonacci(9))