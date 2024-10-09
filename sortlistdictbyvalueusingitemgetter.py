from operator import itemgetter

data_list = [{"name":'Nandini', "age":22},
             {"name":'Rahul', "age": 24},
             {"name": 'Raj', "age": 19},
             {"name": 'Rohan', "age": 22}]

# print("The list sorted by age is")
# print(sorted(data_list, key = itemgetter("age")))

print("The list sorted by age and name is ")
print(sorted(data_list, key = itemgetter("age", "name")))