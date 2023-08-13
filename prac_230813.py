

# 풍선팡2 연습

# T = int(input())
# for tc in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     balloon = 0
#     max_v = 0
#
#     for row in range(N):
#         for col in range(M):
#             balloon = 0
#             center = arr[row][col]
#             for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#                 if 0 <= row + di < N and 0 <= col + dj < M:
#                     balloon += arr[row+di][col+dj]
#             balloon += center
#             if max_v < balloon:
#                 max_v = balloon
#
#     print(f'#{tc} {max_v}')



# DFS 연습 - 백준 (메모리 초과) : 인접 리스트를 익혀야..?

# N, M, R = list(map(int, input().split()))
# arr = [list(map(int, input().split())) for _ in range(M)]
# matrix = [[0] * (N+1) for _ in range(N+1)]
# visit = [False] * (N+1)
# stack = []
# result = []
# visit[R] = True
# result.append(R)
#
# for i in range(M):
#     M1, M2 = arr[i][0],arr[i][1]
#     matrix[M1][M2] = 1
#     matrix[M2][M1] = 1
#
# while True:
#     for node in range(1, N+1):
#         if visit[node] == False and matrix[R][node]:
#             stack.append(R)
#             R = node
#             visit[R] = True
#             result.append(R)
#             break
#
#     else:
#         if len(stack) != 0:
#             R = stack.pop()
#         else:
#             break
#
# for j in range(1, N+1):
#     if j not in result:
#         result.insert(j-1, 0)
#
# for k in result:
#     print(k)



# dfs 연습 - swea

# import sys
# sys.stdin = open('wj.txt', 'r')
#
# T = 1
# for tc in range(1, T+1):
#     V, E = list(map(int, input().split()))
#     temp = list(map(int, input().split()))
#     matrix = [[0] * (V+1) for _ in range(V+1)]
#     for i in range(E):
#         V1, V2 = temp[2*i], temp[2*i+1]
#         matrix[V1][V2] = 1
#         matrix[V2][V1] = 1
#
#     start = 1
#     stack = []
#     result = []
#     visit = [False] * (V+1)
#     visit[start] = True
#     result.append(start)
#
#     while True:
#         for j in range(1, V+1):
#             if visit[j] == False and matrix[start][j] == 1:
#                 stack.append(start)
#                 start = j
#                 visit[start] = True
#                 result.append(start)
#                 break
#
#         else:
#             if len(stack) != 0:
#                 start = stack.pop()
#             else:
#                 break
#
#     real_result = "-".join(map(str,result))
#
#     print(f'#{tc}', real_result)
#


# 코딩 대회 - 코린이 2563 색종이

# matrix = [[0] * 1000 for _ in range(1000)]
# paper = int(input())
# my_subtract = 0
# for _ in range(paper):
#     row, col = list(map(int,input().split()))
#     for row2 in range(10):
#         for col2 in range(10):
#             matrix[row+row2][col+col2] += 1
#
# for row3 in range(1000):
#     for col3 in range(1000):
#         if matrix[row3][col3] >= 2:
#             my_subtract += matrix[row3][col3] - 1
#
# ans = paper * 100 - my_subtract
#
# print(ans)



# 코딩 대회 - 코린이 10163 색종이

# matrix = [[0] * 1001 for _ in range(1001)]
# area = 0
# paper = int(input())
# for i in range(1, paper+1):
#     col, row, width, height = list(map(int,input().split()))
#     for row2 in range(height):
#         for col2 in range(width):
#             matrix[row + row2][col + col2] = i
#
# for j in range(1, paper+1):
#     box = 0
#     for area1 in range(1001):
#         for area2 in range(1001):
#             if matrix[area1][area2] == j:
#                 box += 1
#
#     print(box)


