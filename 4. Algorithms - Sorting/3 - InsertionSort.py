def insertionSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        last = i - 1

        while last >=0 and key < arr[last]:
            arr[last+1] = arr[last]
            last = last-1

        arr[last + 1] = key
        
    return arr


arr = [29, 10, 14, 27, 14]
print(f'final:{insertionSort(arr)}')