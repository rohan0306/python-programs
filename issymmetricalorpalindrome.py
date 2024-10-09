def isPalindrome(s):      #function
    return s == s[::-1]   # reverse string & using slicing operation

def isSymmterical(s):    #function
    length = len(s)      #calculates the length
    mid = length // 2    #calculate middle index
    if length % 2 == 0:
        return s[:mid] == s[mid:]   #first half and second half
    else:
        return s[:mid] == s[mid+1]  #first half and second half excluding middle char

string = "amaama"
if isPalindrome(string):
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")

if isSymmterical(string):
    print("It is Symmetrical")
else:
    print("It is not a Symmetrical")