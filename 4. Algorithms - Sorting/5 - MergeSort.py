def mergeSort(my_array):
    ## Base case
    if len(my_array) == 1:
        return my_array
    
    ## Finding middle element
    middle = len(my_array) // 2

    ## Splitting 
    left = my_array[:middle]
    right = my_array[middle:]

    ## Recursive Call
    left_result = mergeSort(left)
    right_result = mergeSort(right)

    ## Calling merge function
    return merge(left_result, right_result)

def merge(left_result, right_result):
    result = [None] * (len(left_result) + len(right_result))
    
    i = j = k = 0

    # While both pointer are inside the length
    while (i < len(left_result)) and (j < len(right_result)):
        if left_result[i] <= right_result[j]:
            result[k] = left_result[i]
            i+=1
        else:
            result[k] = right_result[j]
            j+=1
        k+=1

    ## if left result is remaining
    while i < len(left_result):
        result[k] = left_result[i]
        i+=1
        k+=1
    
    ## if right result is remaining
    while j < len(right_result):
        result[k] = right_result[j]
        j+=1
        k+=1

    return result

arr = [29, 10, 14, 27, 14]
print(f'final:{mergeSort(arr)}')
    