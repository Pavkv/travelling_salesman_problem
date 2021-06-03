from math import inf
with open('matrixtest.txt', 'r') as f:
    matrix = ([list(map(int, row.split())) for row in f.readlines()])
n = len(matrix)
for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i].insert(j, inf)
res = []
result = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] != inf:
            res.append([i + 1, j + 1])
