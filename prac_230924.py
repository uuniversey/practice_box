
import sys
sys.stdin = open('wj.txt')

# 마법사 상어와 파이어볼

from collections import deque

N, M, K = map(int, input().split())
grid = [[0] * N for _ in range(N)]
dt = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
fireball = deque()
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    grid[r-1][c-1] = [m, s, d]
    fireball.append((r-1, c-1, d))

while K > 0:
    K -= 1
    F = len(fireball)
    vstd = [[1] * N for _ in range(N)]
    tmp = deque()

    for k in range(F):
        i, j, D = fireball.popleft()
        di, dj = dt[D]
        ni = i + grid[i][j][1] * di
        nj = j + grid[i][j][1] * dj

        if ni >= 0:
            ni = ni % N
        else:
            if -ni % N == 0:
                ni = -ni % N
            else:
                ni = N - (-ni % N)

        if nj >= 0:
            nj = nj % N
        else:
            if -nj % N == 0:
                nj = -nj % N
            else:
                nj = N - (-nj % N)

        if grid[ni][nj] == 0:
            grid[ni][nj] = grid[i][j]
            fireball.append((ni, nj, D))
        else:
            for l in range(3):
                grid[ni][nj][l] += grid[i][j][l]
            vstd[ni][nj] += 1
            if [ni, nj] not in tmp:
                tmp.append([ni, nj])

        grid[i][j] = 0

    while tmp:
        I, J = tmp.popleft()
        if grid[I][J][2] % 2:
            for m in range(1, 8, 2):
                fireball.append((I, J, m))
        else:
            for n in range(0, 8, 2):
                fireball.append((I, J, n))

        grid[I][J] = [grid[I][J][0] // 5, grid[I][J][1] // vstd[I][J], D]

fireball = list(set(fireball))
sum_v = 0
for s in range(len(fireball)):
    sum_v += grid[fireball[s][0]][fireball[s][1]][0]
print(sum_v)