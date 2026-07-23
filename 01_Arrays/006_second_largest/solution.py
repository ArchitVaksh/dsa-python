def second_largest(array):
    if len(array) < 2:
        return None

    largest = float("-inf")
    second_largest = float("-inf")

    for current in array:
        if current > largest:
            second_largest = largest
            largest = current

        elif current != largest and current > second_largest:
            second_largest = current

    if second_largest == float("-inf"):
        return None

    return second_largest


# Examples
print(second_largest([10, 5, 20, 8, 15]))   
print(second_largest([8, 2, 6, 7, 1]))     
print(second_largest([100, 90]))            
print(second_largest([5, 5, 3, 2]))        
print(second_largest([1, 1, 1]))             
print(second_largest([-5, -2, -10]))        