def move_zeros(array):
    index = 0
    for i in range(len(array)):
        current = array[i]
        if current != 0:
            array[index],array[i] = array[i],array[index]
            index += 1

    return array

print(move_zeros([0, 1, 0, 3, 12]))   
print(move_zeros([1, 2, 3]))   
print(move_zeros([0, 0, 0]))   
print(move_zeros([1, 0, 2, 0, 3]))   