# mylist = [2, 4, 6, 8, 5, 9]

# print("The list before reversing is ", mylist)

# mylist.reverse()

# print("The list after reversing in ", mylist)


def reverse(list):
    newlist = list[::-1]

    return newlist

list = [2, 4, 6, 8, 5, 9]
print(reverse(list))