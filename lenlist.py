# mylist = [2, 4, 6, 8, 5, 9]
# print(len(mylist))


#Find length of list using naive method

newlist = [2, 4, 6, 8, 5, 9]

print("The original string is", newlist)

counter = 0
for i in newlist:
    counter += 1

print("The total length of list is ", counter)