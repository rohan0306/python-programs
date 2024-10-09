def returnSum(dict):
    list = []
    for i in dict:
        list.append(dict[i])
    final = sum(list)
    return final

dict = {'a': 100, 'b':200, 'c':300}

print("Sum is: ", returnSum(dict))