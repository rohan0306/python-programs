string = 'Gfg is best. Geeks are good and Geeks like Gfg'

print("The original string is: ", string)

res = {key: string.count(key) for key in string.split()}   #dictionary and split() the string in a separate element called list

print("The words frequency is: ", res)