test_dict = { 'month': [1, 2, 3], 'name': ['Jan', 'Feb', 'March'] }

print("The original dictionary is ", test_dict)

res = dict((zip(test_dict['month'], test_dict['name'])))    # zip(test_dict['month'], test_dict['name']): The zip() function takes two lists (in this case, test_dict['month'] and test_dict['name']) and combines them into pairs (tuples).

print("The  flattened dictionary ", res)