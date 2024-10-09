test_list = [2, 3, 4, 5]
print('The original list is', test_list)

test_tuple = (7, 10)
test_list = test_list + list(test_tuple)      # test_list += test_tuple

print('The list is ', test_list)