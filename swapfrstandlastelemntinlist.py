# my_list= [2, 4, 5, 6, 7, 8]

# my_list[0], my_list[-1] = my_list[-1], my_list[0]

# print(my_list) 


def swapList(newList):

    size = len(newList)

    temp = newList[0]   #first element is assigned to temp
    newList[0] = newList[size - 1]   #Last element is assigned to first element
    newList[size-1] = temp

    return newList

newList = [2, 4, 6, 8, 5]
print(swapList(newList))
  
