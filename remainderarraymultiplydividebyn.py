def findremainder(arr, len, n):
    product = 1
    for i in range(len):
        product = product * arr[i]
    return product % n

if __name__ == "__main__":
    arr = [100, 10, 5, 25, 35, 14]
    len = len(arr)
    n = 11
    print(findremainder(arr, len, n))

#input = [100, 10, 5, 25, 35, 14]
#n = 11
#output = 9
