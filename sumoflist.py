# list = [2, 4, 6, 8, 9, 3, 5]

# total = sum(list)

# print(total)

#using for loop
# list = [2, 4, 6, 8, 9, 3, 5]
# total = 0

# for i in range(0, len(list)):
#     total = total + list[i]

# print("Sum of list is",total)

#using while loop

list = [2, 4, 6, 8, 9, 3, 5]
total = 0
i = 0

while (i < len(list)):
    total = total + list[i]
    i += 1

print("Sum of list is", total)
