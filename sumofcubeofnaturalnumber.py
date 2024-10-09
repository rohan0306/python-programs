def cubenum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i*i*i   #only formula difference in cube and square program
    return sum

n = 4
print(cubenum(n))