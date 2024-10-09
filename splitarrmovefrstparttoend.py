def splitArray(a,n,k):   #function
    b = a[:k]                         #new array is created first k elements of a 
    return(a[k::] + b[::])            #adding both

if __name__ == "__main__":
    arr = [ 12, 10, 5, 6, 52, 36]
    n = len(arr)
    position = 2
    arr = splitArray(arr, n, position)
    for i in range (0, n):
        print (arr[i], end=' ')


#input =  5 6 52 36 12 10
