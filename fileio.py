f = open("file.txt", "r")
data = f.read()
print(data)
f.close()

#The above code can be written as

with open ("file.txt") as f:
    print(f.read())