# my_list = [2, 4, 6, 8, 5]

# my_list[1], my_list[3] = my_list[3], my_list[1]

# print(my_list)

def swaplist(newlist):
    size = len(newlist)

    temp = newlist[1]
    newlist[1] = newlist[3]
    newlist[3] = temp

    return newlist

newlist = [2, 4, 6, 8, 5]
print(swaplist(newlist))