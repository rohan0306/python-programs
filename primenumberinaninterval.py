def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) +1):
        if num % i == 0:                   #Check for divisiblity if remiander is equal to zero then num si not prime num
            return False 
    return True

def print_prime_range(start, end):
    print(f"Prime numbers between {start} and {end} is")
    for num in range(start, end + 1):  #The end + 1 is used because range in Python is exclusive of the upper limit, so adding 1 includes end in the range.
        if isprime(num):
            print(num, end = "  ")

start = 3
end = 50
print_prime_range(start, end)