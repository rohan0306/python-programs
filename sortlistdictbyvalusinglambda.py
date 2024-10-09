data_list = [{"name": "Harry", "age": 22},
             {"name": "Nandini", "age": 19},
             {"name": "Rohan", "age": 20},
             {"name": "Sayali", "age": 32}]

# print("The list sorting by age is ")
# print(sorted(data_list, key = lambda i: i['age']))

print("The list sorting by age is ")
print(sorted(data_list, key = lambda i: (i['age'], i['name'])))