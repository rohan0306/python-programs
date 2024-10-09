def insertionsort(arr):
    n = len(arr)

    if n <= 1:
        return
    
    for i in range(1, n):
        key = arr[i]

        j = i-1

        while j >= 0 and key < arr[j]:    #ensures that it dont go out of bounds ON LEFT SIDE OF ARRAY
            arr[j+1] = arr[j]
            j = j-1
            arr[j+1] = key

arr = [12, 11, 13, 5, 6]
insertionsort(arr)
print(arr)


