
import sys
sys.stdin = open('test.txt')

# 백준. 13460 구슬 탈출 2

# def dfs(s):
#
#
# N, M = map(int, input().split())
# board = [list(input()) for _ in range(N)]
#
# for r in range(N):
#     for c in range(M):
#         if board[r][c] == 'R':
#             R = (r, c)
#         elif board[r][c] == 'B':
#             B = (r, c)
#         elif board[r][c] == 'O':
#             O = (r, c)


# 백준. 16639 괄호 추가하기 3

N = int(input())
equation = list(input())

dp = [[0] * N for _ in range(N)]
print(equation)