def check(string):
    string = string.lower()  #lower converts uppercase to lowercase treating all words equally

    vowels = set("aeiou")    #"aeiou" = {'a','e','i','o','u',}

    s = set({ })     #empty dictionary is created and it store any vowel found in string

    for char in string:
        if char in vowels:
            s.add(char)
        else:
            pass

    if len(s) == len(vowels):
        print('Accepted')
    else:
        print('Not Accepted')

string = "SEEquoiaL"
check(string)
