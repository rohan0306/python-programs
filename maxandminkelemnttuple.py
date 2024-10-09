test_tuple = (5, 20, 3, 7, 6, 8)

print("The original tuple is", test_tuple)

k =2

test_tuple = list(sorted(test_tuple))

res = []

for idx, val in enumerate (test_tuple):
    if idx < k or idx >= len(test_tuple) - k:
        res.append(val)
res = tuple(res)
print("The extracted values is", res)
                  
