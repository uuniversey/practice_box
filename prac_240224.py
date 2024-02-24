import sys
sys.stdin = open('test.txt')

# 백준 15684. 사다리 조작

# 1. res 한개씩 늘려주기
# 2. 늘어난 res 중 양옆에 붙어있는 애 빼주기
# 3. 끝

def check(a, b):
    start = a
    while a != H-1:
        if ladder[a][b] == -1:
            b += 1
        else:
            a += 1

    if b != start:
        return False


def comb(s, k, e):
    if s == e:
        for se in sets:
            x, y = se
            ladder[x][y] = -1
            ladder[x][y+1] = 0

            ischeck = True
            for j in range(N):
                ischeck = check(j, 0)

            ladder[x][y] = 1
            ladder[x][y + 1] = 1

            if ischeck == True:
                print(res)
                exit()

    else:
        for i in range(k, len(cand)):
            sets[s] = cand[i]
            comb(s+1, i+1, e)


input = sys.stdin.readline

N, M, H = map(int, input().split())
ladder = [[1] * N for _ in range(H)]
res = 1
impossible = []
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = -1
    ladder[a-1][b] = 0
    impossible.append((a-1, b-1))
    impossible.append((a-1, b))
    if b-2 >= 0:
        impossible.append((a-1, b-2))

cand = []
for r in range(H):
    for c in range(N-1):
        if not (r, c) in impossible:
            cand.append((r, c))

sets = [0] * res
comb(0, 0, res)
