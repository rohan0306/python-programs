str = "Geeks for Geeks"
print('The original string is: ', str)

all_freq = {}    #empty dictionary
for i in str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

res = min(all_freq, key= all_freq.get)   #only change min to max and vice versa
print("The minimum of all character is: ", res)