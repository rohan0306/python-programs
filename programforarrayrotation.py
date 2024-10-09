def reverse(start, end, arr):
    no_of_reverse = end - start + 1
    count = 0
    while ((no_of_reverse) // 2 != count):
       arr[start+count], arr[end-count] = arr[end-count], arr[start+count]
       count += 1
    return arr

def left_rotate_array(arr, size, d):

    start = 0
    end = size - 1
    arr = reverse(start, end, arr)    #Reverse entire array

    start = 0 
    end = size - d - 1
    arr = reverse(start, end, arr)   #Reverse the first part of subarray

    start = size - d
    end = size - 1
    arr = reverse(start, end, arr)  #Reverse the second part of subarray

    return arr

arr =[1,2,3,4,5,6,7,8,]
size = 8
d = 1
print("Original array is: ", arr)

if (d <= size) :
    print("Rotated array is: ", left_rotate_array(arr, size, d))
else:
    d = d % size
    print("Rotated array is: ", left_rotate_array(arr, size, d))