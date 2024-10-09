def check_string(string, pattern):
    i,j = 0,0                   #i is the string and j is pattern

    for char in string:
        if char == pattern[j]:
            j += 1
        if j == len(pattern):
            return True
        i += 1
    return False

string = 'engineers rock'
pattern = 'er'
print(check_string(string, pattern))
