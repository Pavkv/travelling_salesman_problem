from math import inf
import tsp
with open('matrix.txt', 'r') as f: matrix = ([list(map(int, row.split())) for row in f.readlines()])
n = range(len(matrix))
for i in n:
    for j in n:
        if i == j:
            matrix[i].insert(j, 0)
shortestpath = {(i, j): matrix[i][j] for i in n for j in n}
f = tsp.tsp(n, shortestpath)
for i in n:
    f[1][i] += 1
print(int(f[0]))
s = ''
for i in range(0, len(f[1])-1, 2):
    s += str(f[1][i]) + '->' + str(f[1][i + 1]) + '->'
s += str(f[1][-1]) + '->' + str(f[1][0])
print(s)
with open('matrix.txt', 'r') as f:
    matrix = ([list(map(int, row.split())) for row in f.readlines()])
n = len(matrix)
for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i].insert(j, inf)
kr = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] != inf:
            kr.append([i + 1, j + 1])
        else:
            break
r = []
p = []
for x in range(len(kr)):
    k = kr[x].copy()
    check = [0] * (n + 1)
    check[k[0]] += 1
    check[k[1]] += 1
    res = []
    result = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != inf:
                res.append([i + 1, j + 1])
    for j in range(len(res)):
        if res[j] == k:
            del res[j]
            result.append(kr[x])
            break
    minn = inf
    for i in range(len(res)):
        if len(res) < 3:
            break
        for j in range(len(check)):
            if check[j] > 1:
                l = 0
                while l < len(res):
                    if res[l][0] == j or res[l][1] == j:
                        del res[l]
                    else:
                        l += 1
        for j in range(len(res)):
            if matrix[res[j][0]-1][res[j][1]-1] < minn:
                if res[j][0] == result[-1][1] and res[j][1] != result[-1][0] and res[j][1] != result[0][0]:
                    minn = matrix[res[j][0]-1][res[j][1]-1]
                    k[0] = res[j][0]
                    k[1] = res[j][1]
        for j in range(len(res)):
            if res[j] == k:
                del res[j]
                result.append(k.copy())
                break
        check[k[0]] += 1
        check[k[1]] += 1
        minn = inf
        k = [0, 0]
    if res[0][1] == result[0][0]:
        result.append(res[0])
    elif res[1][1] == result[0][0]:
        result.append(res[1])
    r.append(result)
    path = 0
    for i in range(len(result)):
        path += matrix[result[i][0]-1][result[i][1]-1]
    p.append(path)
val, idx = min((val, idx) for (idx, val) in enumerate(p))
print(val)
output = ''
result = r[idx]
for i in range(0, len(result)):
    output += str(result[i][0]) + '->' + str(result[i][1]) + ' '
print(output)