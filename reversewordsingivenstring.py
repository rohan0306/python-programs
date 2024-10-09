string = "geeks quiz practise code" #input
s = string.split()[::-1]      #slicing opeartion & reverse string
l = []                        #emptylist
for i in s:
    l.append(i)
print(" ".join(l))
