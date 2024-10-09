# list =  [2, 4, 6, 8, 9, 3, 5]
# list.sort()
# print("Smallest num is", list[0])


# list =  [2, 4, 6, 8, 9, 3, 5]
# list.sort(reverse = True)
# print("Smallest element is", list[-1])


# list =  [2, 4, 6, 8, 9, 3, 5]
# print("Smallest number is ", min(list))

list = []

# asking number of elements to put in list
num = int(input("Enter number of elements in list: "))

# iterating till num to append elements in list
for i in range(1, num + 1):
	ele= int(input("Enter elements: "))
	list.append(ele)
	
# print minimum element:
print("Smallest element is:", min(list))
