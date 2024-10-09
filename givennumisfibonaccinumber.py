import math                        #math module

def is_perfect_square(x):          #function 
    s = int(math.sqrt(x))          #convert into integer from decimal and and stores in s
    return s*s == x                 #checks square of s is equal to x

def is_Fibonacci(num):
    return is_perfect_square(5*num*num+4) or is_perfect_square(5*num*num-4)

num = int(input("Enter a number: "))

if is_Fibonacci(num):
    print(f"{num} is Fibonacci number")
else:
    print(f"{num} is not a Fibonacci number")