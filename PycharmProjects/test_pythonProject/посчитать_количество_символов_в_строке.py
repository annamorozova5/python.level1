str = "I like to swim"
dict = {}
for l in str:
    k = str.count(l, 0, len(str))
    dict[l] = k

print(dict)
