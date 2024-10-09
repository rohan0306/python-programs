myDict = {'gfg': [7, 6, 3], 
             'is': [2, 10, 3], 
             'best': [19, 4]}

print("The original is ", myDict)

res = { key: sorted(myDict[key]) for key in sorted(myDict)}      
print(res)