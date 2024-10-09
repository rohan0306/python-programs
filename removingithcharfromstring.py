def remove(string, i):

    a = string[:i]       #index 0 to 4 i.e geeksForgeeks = geeks

    b = string[i+1:]     #index 0 to 6 i.e geeksForgeeks = orgeeks

    return a + b

if __name__ == "__main__":
    string = "geeksforgeeks"
    i = 5
    print(remove(string,i))