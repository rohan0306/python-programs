str = "Geeks for Geeks"

print("The original string is: ", str)

all_freq = {}
for i in str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1 

res = max(all_freq, key = all_freq.get)    #only change max to min and vice versa 

print("The maximum of all character is: ", res)