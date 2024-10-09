def binary_search(arr, low, high, x):  #function, arr = input, low = starting index, high = ending index

    if high >= low:        #if this condition matches it ensures that there is atleast one element in search range

        mid = (high + low) // 2        #it finds the middle element

        if arr[mid] == x:              #check if element is at middle
            return mid
        
        elif arr[mid] > x:            # searching left half
            return binary_search(arr, low, mid-1, x)
        
        else:                                         #searching right half
            return binary_search(arr, mid+1, high, x)
    else:
        return -1                  #if element not found
    

arr = [ 2, 3, 4, 10, 40]
x  = 10

result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present")