def binary_search(arr, x):
    low = 0                # starting index is set at index 0 
    high  = len(arr) - 1   # end index  
    mid = 0                # it is calculate using while loop

    while high > low:

        mid = (high+low) // 2

        if arr[mid] < x:     #if x is greater then ignore left half
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid
        
    return -1

arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", result)

else:
    print('Element is not present in array')
        
