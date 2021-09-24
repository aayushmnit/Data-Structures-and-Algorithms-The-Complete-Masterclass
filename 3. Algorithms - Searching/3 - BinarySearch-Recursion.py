def binarySearch(my_array, target):
    left = 0
    right = len(my_array) - 1
    result = helper(my_array, target, left, right)
    return result

def helper(my_array, target, left, right):
    if left > right:
        return -1
    
    middle = (left + right) // 2
    middle_element = my_array[middle]

    if  middle_element == target:
        return middle
    elif middle_element > target:
         right = middle - 1
         result = helper(my_array, target, left, right)
         return result
    else:
        left = middle + 1
        result = helper(my_array, target, left, right)
        return result
    
### Test 1 ###
print(binarySearch([1, 5, 10, 12, 25, 30, 32], 29))

### Test 2 ###
print(binarySearch([5, 10, 15, 20, 25], 15))

