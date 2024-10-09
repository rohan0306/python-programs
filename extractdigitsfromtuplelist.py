from itertools import chain

test_list = [(15,3), (22,8), (4, 57)]

print("The original list is ", test_list)

temp = map(lambda ele : str(ele), chain.from_iterable(test_list))

res = set()
for sub in temp:
    for ele in sub:
        res.add(ele)

print(res)