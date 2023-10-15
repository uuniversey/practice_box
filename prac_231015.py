
import sys
sys.stdin = open('test.txt')

# 백준 15684. 사다리 조작

# def moving(x):
#     c = x
#     for y in range(H):
#         c += lad[y][c]
#
#     if c == x:
#         return 1
#     else:
#         return 0
#
#
# def comb(s, k, e):
#     global res
#     if res != -1:
#         return
#
#     if s == e:
#         li = []
#         for check in sets:
#             li.append(cand[check])
#         li.sort()
#
#         for m in range(e-1):
#             if li[m][1] + 1 == li[m][1]:
#                 break
#
#         else:
#
#             for idx in sets:
#                 ir, ic = cand[idx]
#                 lad[ir][ic] = 1
#                 lad[ir][ic+1] = -1
#             for x in range(1, N+1):
#                 if not moving(x):
#                     for idx2 in sets:
#                         jr, jc = cand[idx2]
#                         lad[jr][jc] = 0
#                         lad[jr][jc + 1] = 0
#                     break
#
#             else:
#                 res = e
#                 return
#
#     else:
#         for i in range(k, len(cand)):
#             sets[s] = arr[i]
#             comb(s+1, k+1, e)
#
#
# N, M, H = map(int, input().split())
# lad = [([9] + ([0] * N) + [9]) for _ in range(H)]
# res = -1
# for _ in range(M):
#     a, b = map(int, input().split())
#     lad[a-1][b], lad[a-1][b+1] = 1, -1
#
# if not M:
#     print(0)
#     exit()
#
# else:
#     cand = []
#     for col in range(1, N+1):
#         for row in range(H):
#             if lad[row][col] == 0:
#                 if lad[row][col+1] == 0:
#                     cand.append((row, col))
#
#     arr = [j for j in range(len(cand))]
#
#     n = 1
#     while n <= 3:
#         sets = [0] * n
#         comb(0, 0, n)
#         if res != -1:
#             break
#         else:
#             n += 1
#
#     print(res)


# 백준 9461. 파도반 수열

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     memo = [0] * 101
#     memo[1], memo[2], memo[3], memo[4], memo[5] = 1, 1, 1, 2, 2
#     for n in range(6, 101):
#         memo[n] = memo[n-1] + memo[n-5]
#
#     print(memo[N])


# 백준 11286. 절대값 힙

# import heapq
#
# N = int(input())
# hq = []
# for _ in range(N):
#     x = int(sys.stdin.readline().rstrip())
#     if x:
#         heapq.heappush(hq, (abs(x), x))
#     else:
#         if not hq:
#             print(0)
#         else:
#             print(heapq.heappop(hq)[1])


# 백준 11279. 최대 힙

# import heapq
#
# N = int(input())
# hq = []
# for _ in range(N):
#     x = int(sys.stdin.readline().rstrip())
#     if x:
#         heapq.heappush(hq, -x)
#     else:
#         if not hq:
#             print(0)
#         else:
#             print(-heapq.heappop(hq))


# 백준 11659. 구간 합 구하기 4

# N, M = map(int, sys.stdin.readline().rstrip().split())
# arr = list(map(int, sys.stdin.readline().split()))
# for _ in range(M):
#     i, j = map(int, sys.stdin.readline().rstrip().split())
#     print(sum(arr[i-1:j]))