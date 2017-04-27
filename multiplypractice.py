def multiply(x, y):
	'''Takes in two integers and returns their product.'''
	if x == 0 or y == 0:
		return 0
	else:
		return x + multiply(x, y - 1)
			
print(multiply(0, 0))
print(multiply(4, 5))
print(multiply(7, 9))
print(multiply(1, 1))