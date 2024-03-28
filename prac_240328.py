import sys
sys.stdin = open('test.txt')

# 백준. 14725 개미굴

# input = sys.stdin.readline
# N = int(input())
# cave = []
#
# # 굴 채워넣기
# for _ in range(N):
#     k, *arr = input().split()
#     cave.append(arr)
# cave.sort() # 사전 순서대로 출력해야하니 정렬
#
# check = []  # 이미 나왔던 라인인지 체크를 위한 배열
# for c in cave:
#     for idx, val in enumerate(c):   # idx에 따라 --의 갯수를 출력 val는 이름
#         if c[:idx+1] in check:
#             continue
#         print('--' * idx + val)
#         check.append(c[:idx+1])     # check에 기록



# 백준. 20166 문자열 지옥에 빠진 호석

from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(N)]
ans = [input().rstrip() for _ in range(K)]
cnt = [0] * K

delta = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for r in range(N):
    for c in range(M):
        q = deque([(r, c, grid[r][c])])
        while q:
            pr, pc, standard = q.popleft()
            if len(standard) == 5:
                continue

            for dr, dc in delta:
                mystr = standard
                nr, nc = pr+dr, pc+dc

                nr %= N
                nc %= M

                mystr += grid[nr][nc]

                for idx, val in enumerate(ans):
                    if mystr == val:
                        cnt[idx] += 1

                q.append((nr, nc, mystr))

[print(i) for i in cnt]
