def find_max(array):
    max_number = array[0]
    for num in range(len(array)):
        if array[num] > max_number:
            max_number = array[num]
    return max_number
            
print(find_max([7, 3, 11, 2, 9, 5]))
print(find_max([100]))
print(find_max([-8, -3, -15]))