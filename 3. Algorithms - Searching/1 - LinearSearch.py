def linearSearch(my_array, target):

    for i in range(len(my_array)):
        if my_array[i] == target:
            return i
    
    return -1

print(linearSearch([5, 3, 1, 9, 2], 9))