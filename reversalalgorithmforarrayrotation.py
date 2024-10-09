def rverseArray(arr, start, end):  # rverseArray() is a helper function used to reverse the section of an array
    while (start < end):
        temp = arr[start]  # Swapping logic
        arr[start] = arr[end]
        arr[end] = temp

        start = start + 1  # Move start index to  right to the middle of array
        end = end - 1  # Move end index to left to the middle of array


def leftRotate(arr, d):
    n = len(arr)
    rverseArray(arr, 0, d - 1)

    rverseArray(arr, d, n - 1)

    rverseArray(arr, 0, n - 1)


def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i])


arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2)
printArray(arr)
