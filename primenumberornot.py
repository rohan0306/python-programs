def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("It is not a PRIME NUMBER")
            #return False 
    print("It is a prime number")
    #return True

num = 9
isprime(num)


# def is_prime(num):
#     # Check if the number is less than 2 (not prime)
#     if num < 2:
#         return False
#     # Check divisors from 2 to the square root of num
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False  # Not prime if divisible
#     return True  # Prime if no divisors found

# # Input from the user
# num = int(input("Enter a number: "))

# # Check if the number is prime and print the result
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")


