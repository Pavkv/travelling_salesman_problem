import random

import numpy as np


class TravellingSalesman:
    def __init__(self, initialT, d_ij, showTourOutput=False):
        self.T = initialT
        self.d_ij = d_ij

        self.D = self.calculateLengthOfTour(initialT)
        self.showTourOutput = showTourOutput

    def calculateLengthOfTour(self, tour):
        sumDistance = 0
        for ind in range(len(tour)):
            v_1 = tour[ind]

            if (ind == (len(tour) - 1)):
                v_2 = tour[0]
            else:
                v_2 = tour[ind + 1]

            sumDistance += self.d_ij[v_1][v_2]

        return sumDistance

    def runTS(self):
        N = len(self.T)

        for i in range(N - 3):
            for j in range(i + 2, N - 1):
                newT = np.copy(self.T)

                newT[i + 1] = self.T[j]
                ind = i + 2
                for k in range(j - 1, i, -1):
                    newT[ind] = self.T[k]
                    ind += 1

                newT_D = self.calculateLengthOfTour(newT)

                if (newT_D < self.D):
                    self.T = np.copy(newT)
                    self.D = np.copy(newT_D)
                    self.runTS()


with open('matrix.txt', 'r') as f: matrix = ([list(map(int, row.split())) for row in f.readlines()])
n = range(len(matrix))
for i in n:
    for j in n:
        if i == j:
            matrix[i].insert(j, 0)
D = []
for i in n:
    for j in n:
        D.append(matrix[i][j])
T = []
for i in n:
    T.append(i)
r = []
p = []
for _ in range(100):
    random.shuffle(T)
    T = np.array(T)
    D_ij = np.array(D)
    D_ij = D_ij.reshape(len(matrix), len(matrix))

    TS = TravellingSalesman(T, D_ij, False)
    TS.runTS()
    p.append(int(TS.D))
    r.append(TS.T)

val, idx = min((val, idx) for (idx, val) in enumerate(p))
print(val)
output = ''
result = r[idx]
res = []
for num in result:
    res.append(num+1)
for i in range(len(res)-1):
    output += str(res[i]) + '->' + str(res[i+1]) + ' '
output += str(res[-1]) + '->' + str(res[0])
print(output)
