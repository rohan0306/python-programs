# list = [2, 4, 6, 8, 9, 3]
# list.sort()
# print("Largest number is", list[-1])


# list = [2, 4, 6, 8, 9, 3]
# list.sort(reverse = True)
# print("Smallest number is", list[0])

#list = [2, 4, 6, 8, 9, 3]
#print("Smallest number is", max(list))


list = []
num = int(input("Enter a number of elements"))
for i in range(1, num + 1):
    ele = int(input("Enter number"))
    list.append(ele)

print("Largest element is", max(list))
 

