import sys
sys.stdin = open('test.txt')

# 백준 26594. ZOAC 5

# arr = input()
# num = 0
# memo = arr[0]
# for a in arr:
#     if memo != a:
#         break
#     num += 1
#
# print(num)


# 백준 20205. 교수님 그림이 깨지는데요?

# N, K = map(int, input().split())
# pixel = [list(map(int, input().split())) for _ in range(N)]
# ans = []
#
# for pix in pixel:
#     tmp = []
#     for p in pix:
#         for i in range(K):
#             tmp.append(p)
#     for j in range(K):
#         print(*tmp)


# 백준 1193. 분수 찾기

# X = int(input())
# num = 1
# while True:
#     calc = X - num
#     if calc > 0:
#         X = calc
#     else:
#         break
#     num += 1
#
# if num % 2:
#     print(f'{num - (X-1)}/{1 + (X-1)}')
# else:
#     print(f'{1 + (X - 1)}/{num - (X - 1)}')


# 백준 11931. 수 정렬하기 4

# N = int(input())
# arr = [int(input()) for _ in range(N)]
# arr.sort(reverse=True)
# for i in range(N):
#     print(arr[i])


# 백준 28136. 원, 탁!

# N = int(input())
# arr = list(map(int, input().split()))
# ans = 0
# for i in range(1, N):
#     if arr[i] <= arr[i-1]:
#         ans += 1
#
# if arr[-1] >= arr[0]:
#     ans += 1
# print(ans)


# 백준 9342. 염색체

# import re
#
# T = int(input())
# pattern = re.compile(r'^[ABCDEF]?A+F+C+[ABCDEF]?$')
#
# for _ in range(T):
#     target = input().strip()
#     if pattern.match(target):
#         print('Infected!')
#     else:
#         print('Good')



# 백준 15729. 방탈출

# N = int(input())
# ans = list(map(int, input().split()))
# arr = [0] * (N+2)
# res = 0
#
# for i in range(N):
#     if ans[i] != arr[i]:
#         res += 1
#         arr[i] = 1-arr[i]
#         arr[i+1] = 1-arr[i+1]
#         arr[i+2] = 1-arr[i+2]
#
# print(res)


# 백준 15645. 내려가기 2

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# dp = [[[0, 0] for _ in range(3)] for _ in range(N)]
#
# for r in range(N):
#     if r == 0:
#         dp[r][0][0], dp[r][0][1] = board[0][0], board[0][0]
#         dp[r][1][0], dp[r][1][1] = board[0][1], board[0][1]
#         dp[r][2][0], dp[r][2][1] = board[0][2], board[0][2]
#     else:
#         dp[r][0][0] = max(dp[r-1][0][0], dp[r-1][1][0]) + board[r][0]
#         dp[r][0][1] = min(dp[r-1][0][1], dp[r-1][1][1]) + board[r][0]
#         dp[r][1][0] = max(dp[r-1][0][0], dp[r-1][1][0], dp[r-1][2][0]) + board[r][1]
#         dp[r][1][1] = min(dp[r-1][0][1], dp[r-1][1][1], dp[r-1][2][1]) + board[r][1]
#         dp[r][2][0] = max(dp[r-1][1][0], dp[r-1][2][0]) + board[r][2]
#         dp[r][2][1] = min(dp[r-1][1][1], dp[r-1][2][1]) + board[r][2]
#
# ans = [0, float('inf')]
# for li in dp[-1]:
#     ans[0] = max(ans[0], li[0])
#     ans[1] = min(ans[1], li[1])
#
# print(*ans)

