def words(k, str):   #function , k is given length, str is input
     
    string =[]     #empty list is created

    text = str.split(" ") # it splits the string whenever space occurs

    for x in text:
        if len(x) > k:
            string.append(x)
    return string

k = 3 
str = "Geek for Geeks"
print(words(k, str))
