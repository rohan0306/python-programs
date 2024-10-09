#using for loop

list = [2, 4, 6, 8, 9, 3, 5]
product = 1

for i in range(0, len(list)):     #same formula for addition
     product = product * list[i]

print("Sum of list is", product)