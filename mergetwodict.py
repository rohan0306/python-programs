# def Merge(dict1, dict2):
#     return(dict1.update(dict2))

# dict1 = { 'a': 2, 'b': 3}
# dict2 = { 'c': 4, 'd': 5}

# print(Merge(dict1, dict2))

# print(dict1)

#using | operator
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merging using the | operator
merged_dict = dict1 | dict2

print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}
