def find_largest(arr,n):
    largest = arr[0]

    for i in range(1,n):
        if arr[i] > largest:
            largest = arr[i]
    return largest

if __name__ == "__main__":
   arr = [10, 324, 45, 90, 9808]    
   n = len(arr)
   ans  = find_largest(arr,n)

print("Largest element is ", ans)