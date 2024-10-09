myDict = {'ravi': 10, "rajnish": 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

myKeys = list(myDict.keys())
myKeys.sort()

sorted_dict = {i: myDict[i] for i in myKeys}

print(sorted_dict)



# myDict = {'gfg': [7, 6, 3], 
#              'is': [2, 10, 3], 
#              'best': [19, 4]}


# myKeys = list(myDict.keys())
# myKeys.sort()

# sorted_dict = {i: myDict[i] for i in myKeys}

# print(sorted_dict)