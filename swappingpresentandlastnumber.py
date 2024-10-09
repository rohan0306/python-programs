def reverse(arr,size):
    i = 0
    while i < size // 2:   #only first half is to be reversed
       arr[i] , arr[size - i -1] = arr[size - i -1] , arr[i]    
       i += 1
    return arr

arr = [2, 4, 5, 6, 9, 7]
size = 6

print("Original list", arr)
print("Reverse list", reverse(arr,size))

