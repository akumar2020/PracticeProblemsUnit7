def sumlist(list):
	'''Takes in a list and returns the sum of the numbers in the list.'''
	if len(list) == 0:
		return 0
	else:
		return list[0] + sumlist(list[1:])
list = [1, 2, 3, 4, 5]
print(sumlist(list))
list = [1, 3, 5, 7, 9]
print(sumlist(list))
list = [10, 20, 30, 40, 50]
print(sumlist(list))