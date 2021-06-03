from math import inf
import numpy as np


def findmin(m, g):  # find min in row and column(if g = 1 - row, g = 0 - column)
    x_np = np.asarray(m)
    list = np.min(x_np, axis=g)
    return list.tolist()


def minus(m):  # minus min element in row and column
    N = len(m)
    minRow = findmin(m, 1)
    for i in range(N):
        for j in range(N):
            m[i][j] -= int(minRow[i])
    minColumn = findmin(m, 0)
    for i in range(N):
        for j in range(N):
            m[j][i] -= int(minColumn[i])
    return sum(minRow + minColumn)


def findmax(m):  # min cell with max value
    N = len(m)
    Q = []
    M = []
    for i in range(N):
        for j in range(N):
            if m[i][j] == 0:
                minr, minc = 10000, 10000
                for z in range(N):
                    if j != z and minr > m[i][z]:
                        minr = m[i][z]
                    if i != z and minc > m[z][j]:
                        minc = m[z][j]
                Q.append([minr + minc, i, j])
    X = -1
    for i in range(len(Q)):
        if X < Q[i][0]:
            X = Q[i][0]
    for i in range(len(Q)):
        if Q[i][0] == X:
            M.append(Q[i][1])
            M.append(Q[i][2])
            break
    return M


def delete(m, index1, index2):  # delete row and column
    del m[index1]
    for i in m:
        del i[index2]
    return m


with open('matrix.txt', 'r') as f: matrix = ([list(map(int, row.split())) for row in f.readlines()])
n = len(matrix)
# n = 25
# matrix = [[np.random.randint(0, 150) for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i].insert(j, 0)
StartMatrix = []
for i in range(n): StartMatrix.append(matrix[i].copy())
for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = inf
res = []
Row = []
Column = []
for i in range(n):
    Row.append(i)
    Column.append(i)
result = []
H = 0
PathLenght = 0
while True:
    minus(matrix)
    index = findmax(matrix)
    res.append(Row[index[0]] + 1)
    res.append(Column[index[1]] + 1)

    oldIndex1 = Row[index[0]]
    oldIndex2 = Column[index[1]]
    if oldIndex2 in Row and oldIndex1 in Column:
        NewIndex1 = Row.index(oldIndex2)
        NewIndex2 = Column.index(oldIndex1)
        matrix[NewIndex1][NewIndex2] = inf
    del Row[index[0]]
    del Column[index[1]]
    matrix = delete(matrix, index[0], index[1])

    if len(matrix) == 1: break

for i in range(0, len(res) - 1, 2):
    if res.count(res[i]) < 2:
        result.append(res[i])
        result.append(res[i + 1])
for i in range(0, len(res) - 1, 2):
    for j in range(0, len(res) - 1, 2):
        if result[len(result) - 1] == res[j]:
            result.append(res[j])
            result.append(res[j + 1])

for i in range(0, len(result) - 1, 2):
    if i == len(result) - 2:
        PathLenght += StartMatrix[result[i] - 1][result[i + 1] - 1]
        PathLenght += StartMatrix[result[i + 1] - 1][result[0] - 1]
    else:
        PathLenght += StartMatrix[result[i] - 1][result[i + 1] - 1]
print(PathLenght)

output = ''
print(res)
print(result)
for i in range(0, len(result)-1, 2):
    output += str(result[i]) + '->' + str(result[i+1]) + ' '
output += str(result[-1]) + '->' + str(result[0])
print(output)