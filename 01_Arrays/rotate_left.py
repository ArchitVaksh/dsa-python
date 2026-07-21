def rotate_left(array):
    if len(array) != 0 and len(array) != 1:
        for i in range(1,len(array)):
            array[i],array[i-1] = array[i-1],array[i]
    return array

print(rotate_left([1, 2, 3, 4, 5]))   
print(rotate_left([10, 20, 30]))   
print(rotate_left([5]))   
print(rotate_left([]))   