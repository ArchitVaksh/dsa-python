def find_min(array):
	min_number = array[0]
	for i in range(len(array)):
		if array[i] < min_number:
			min_number = array[i]
	return min_number

print(find_min([7, 3, 11, 2, 9, 5]))      # 2
print(find_min([100]))                    # 100
print(find_min([-8, -3, -15]))            # -15
print(find_min([5, 5, 5]))                # 5
print(find_min([10, 9, 8, 7, 6]))         # 6
