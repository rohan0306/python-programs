#using extend and sort
def isMonotonic(A):
    x,y = [],[]
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if (x == A or y == A):
        return True
    return False

A = [6,5,4,4]
print(isMonotonic(A))



# def isMonotonic(arr):
#     increasing = decreasing = True
    
#     for i in range(1, len(arr)):
#         if arr[i] > arr[i - 1]:
#             decreasing = False  # Not decreasing if current element is greater than previous
#         if arr[i] < arr[i - 1]:
#             increasing = False  # Not increasing if current element is smaller than previous

#     return increasing or decreasing

# # Example usage:
# arr1 = [1, 2, 2, 3]
# arr2 = [9, 7, 5, 3]
# arr3 = [3, 3, 2, 1]

# print(isMonotonic(arr1))  # True (Monotonically Increasing)
# print(isMonotonic(arr2))  # True (Monotonically Decreasing)
# print(isMonotonic(arr3))  # True (Monotonically Decreasing)

