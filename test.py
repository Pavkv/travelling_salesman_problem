import tsp
with open('matrix.txt', 'r') as f: matrix = ([list(map(int, row.split())) for row in f.readlines()])
n = range(len(matrix))
for i in n:
    for j in n:
        if i == j:
            matrix[i].insert(j, 0)
shortestpath = {(i, j): matrix[i][j] for i in n for j in n}
output = tsp.tsp(n, shortestpath)
for i in n:
    output[1][i] += 1
print(int(output[0]))
s = ''
for i in range(0, len(output[1])-1, 2):
    s += str(output[1][i]) + '->' + str(output[1][i + 1]) + '->'
s += str(output[1][-1]) + '->' + str(output[1][0])
print(s)