def remove_duplicates_sorted_array(array):
    if len(array) == 0:
        return 0
    k = 1
    for i in range(len(array)-1):
        if array[i] != array[i+1]:
            array[k] = array[i+1]
            k += 1
    return k

nums = [1,1,2,2,3,4,4,5,6,7,7]

print("numeber of unique elements:",remove_duplicates_sorted_array(nums))
print(nums)
