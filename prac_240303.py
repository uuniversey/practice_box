import sys
sys.stdin = open('test.txt')

# 백준. 1149 RGB거리

# input = sys.stdin.readline
# N = int(input())
# cost = [0] * N
# res = 0
# for i in range(N):
#     cost[i] = list(map(int, input().split()))
#
# for j in range(1, N):
#     cost[j][0] += min(cost[j-1][1], cost[j-1][2])
#     cost[j][1] += min(cost[j-1][0], cost[j-1][2])
#     cost[j][2] += min(cost[j-1][0], cost[j-1][1])
#
# print(min(cost[-1]))


# 백준. 9465 스티커

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    dp[0][0] = board[0][0]
    dp[1][0] = board[1][0]
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    dp[0][1] = board[1][0] + board[0][1]
    dp[1][1] = board[0][0] + board[1][1]
    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    for i in range(2, n):
        dp[0][i] = max(dp[1][i - 2], dp[1][i - 1]) + board[0][i]
        dp[1][i] = max(dp[0][i - 2], dp[0][i - 1]) + board[1][i]

    print(max(dp[0][-1], dp[1][-1]))