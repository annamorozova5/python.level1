mat = [[10, 9, 2000], [159, 5698, 45]]

trans_mat = [[0 for j in range(len(mat))] for i in range(len(mat[0]))]

for i in range(len(mat)):
    for j in range(len(mat[0])):
        trans_mat[j][i] = mat[i][j]

print(trans_mat)
