n = 6
d = [10, 9, 2000, 159, 5698, 45]
for run in range(n - 1):
    for r in range(n - 1):
        if d[r] > d[r + 1]:
            d[r], d[r + 1] = d[r + 1], d[r]
print(d)
