def SimpleAdding(num):
	i = 0
	numbers = []
	while i <= num:
		numbers.append(i)
		i += 1

	return sum(numbers)
	
print SimpleAdding(12)
