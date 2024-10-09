#Python program for Single character Ascii value 

c = 'a'
print("The ASCII value of ", c, "is", ord(c))
#print("The ASCII value of '"+c+"'  is", ord(c))


#Python program for string ASCII Value

print("Enter a string", end=" ")
text = input()
#text = "Hello"
textlength = len(text)

for char in text:
    ascii = ord(char)
    print(char, "\t", ascii )



