def rotate_array(array):
    i = len(array) - 1
    while len(array) > 1 and i > 0:
        array[i],array[i-1] = array[i-1],array[i]
        i -= 1
    return array 

print(rotate_array([1, 2, 3, 4, 5]))
# [5, 1, 2, 3, 4]

print(rotate_array([10, 20, 30]))
# [30, 10, 20]

print(rotate_array([5]))
# [5]

print(rotate_array([]))
# []