def bubbleSort(arr):

    for iter in range(len(arr)):
        swap = 0
        for index in range(len(arr) -1 - iter):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1] , arr[index]
                swap += 1
                print(arr)
        if swap == 0:
            return arr

arr = [10, 14, 29, 37, 14]

print(f'final:{bubbleSort(arr)}')