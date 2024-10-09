# from collections import OrderedDict

# iniorderdict = OrderedDict([('akshat', '1'), ('nikhil','3') ])

# iniorderdict.update({'manjeet': '4'})           
# iniorderdict.move_to_end('manjeet', last = False)    # last =True then it would have moved to end 

# print("Update is : ", iniorderdict)


#using naive approach 

from collections import OrderedDict

iniorderdict1 = OrderedDict([('akshat', 1), ('raj', 2)])
iniorderdict2 = OrderedDict([('manjeet', 3), ('raheja', '4')])

both = OrderedDict(list(iniorderdict2.items())  +  list(iniorderdict1.items()))

print('Updated is', both)