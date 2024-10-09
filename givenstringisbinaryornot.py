def check(string):

    p = set(string)       #set function removes duplicate value e.g "101010000111" becomes "0", "1"

    s = {'0', '1'}

    if s == p or p == {'0'} or p == {'1'}:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    string = "101010000111"

    check(string)