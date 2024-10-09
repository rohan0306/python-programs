def linear_search(arr, target):    #function , arr = input, target = the no. to be found
    
    for index in range(len(arr)):    #Traverse through all elements in array
          
        if arr[index] == target:     #if element is found return its index
            return index
    return -1    #if element is not found

arr = [10, 23, 45, 11, 70, 15]
target = 70
result = linear_search(arr, target)

if result !=1:
    print("Element found at index ", result)
else:
    print("Element not found in array")



          
    