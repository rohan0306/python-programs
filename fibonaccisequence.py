nterms = int(input("Enter a number"))

n1, n2 = 0, 1     #First two twerms
count = 0

if nterms <= 0 :
    print("Please enter positive number")
elif nterms == 1:
    print("Fibonacci sequence upto 1")
    print(n1)
else:
    print("Fibonacci sequence ")
    while count < nterms:
        print (n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1