string = "geeks_for_geeks_is_best"

print("The original string is: ", string)

rev = string.replace("_", " ").title().replace(" ", "")    #title() converts first character of each word to upper case

print("The words after changing case is", rev)        #replace underscore to empty place