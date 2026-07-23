def linear_search(array,target):
    for i in range(len(array)):
            if array[i] == target:
                    return i
    return -1  

array = [11, 62, 83, 49, 58, 66]

print(linear_search(array, 83))    # 2
print(linear_search(array, 62))    # 1
print(linear_search(array, 100))   # -1
