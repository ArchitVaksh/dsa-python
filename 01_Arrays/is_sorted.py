def is_sorted(array):
	for i in range(len(array)-1):
		if array[i] > array[i+1]:
			return False
	return True

print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([1, 2, 5, 4, 6]))
print(is_sorted([5]))
print(is_sorted([1, 1, 2, 2, 3]))
print(is_sorted([9, 8, 7])) 
