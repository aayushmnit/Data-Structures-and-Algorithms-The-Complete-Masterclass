def quickSort(my_array):
    qshelper(my_array, 0, len(my_array) - 1) ## Array, Starting value and ending value
    return my_array

def qshelper(my_array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while right >= left:
        # Condition : 1    
        if (my_array[left] > my_array[pivot]) and (my_array[right] < my_array[pivot]):
            my_array[left], my_array[right] = my_array[right], my_array[left]
        
        # Condition : 2
        if my_array[left] <= my_array[pivot]: 
            left += 1

        # Condition : 3        
        if my_array[right] >= my_array[pivot]: 
            right -= 1

    my_array[pivot], my_array[right] = my_array[right], my_array[pivot]

    qshelper(my_array, start, right-1)
    qshelper(my_array, right+1, end)

arr = [29, 10, 14, 27, 14]
print(f'final:{quickSort(arr)}')