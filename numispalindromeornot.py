num = 12321
#num = int(input("Enter a number: "))

temp = num 
reverse = 0

while temp > 0:
    remainder = temp%10
    reverse= (reverse*10)+remainder
    temp = temp // 10

if num == reverse:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")