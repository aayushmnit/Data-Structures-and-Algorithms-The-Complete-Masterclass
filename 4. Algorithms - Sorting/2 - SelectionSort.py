def selectionSort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for index in range(min_index+1, len(arr)):
            if arr[min_index] > arr[index]:
                min_index = index
            
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

arr = [20, 12, 10, 15, 2]
print(f'final:{selectionSort(arr)}')