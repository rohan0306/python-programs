my_str = "Madam"   #initialize
my_str = my_str.casefold()    #casefold
rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("The string is Palindrome")
else:
    print("The string is not a palindrome")

