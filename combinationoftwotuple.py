test_tuple1 = (4, 5)
test_tuple2 = (7, 8)

print("The original tuple is ", test_tuple1)
print("The original tuple is ", test_tuple2)

res = [(a, b) for a in test_tuple1 for b in test_tuple2]
sir = res + [(a, b) for a in test_tuple2 for b in test_tuple1]

print(sir)