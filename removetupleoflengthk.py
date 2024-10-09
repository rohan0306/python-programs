test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k = 1
print("The original is ", test_list)

res = [ele for ele in test_list if len(ele) != k]

print(res)