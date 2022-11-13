n = 7
d = [15, 2, 9, 2000, 99, 568, 852]
print(d)

for r in range(n - 1):
    for j in range(n - 1 - r):
        if d[j] > d[j + 1]:
            d[j], d[j + 1] = d[j + 1], d[j]
print(d)
