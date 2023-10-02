
import sys
sys.stdin = open('test.txt')

# 백준 1436. 영화감독 숌

# N = int(input())
# li = []
# for i in range(2666800):
#     if '666' in str(i):
#         li.append(i)
#
# print(li[N-1])


# 백준 11050. 이항 계수 1

# N, K = map(int, input().split())
#
# m, s = 1, 1
# for i in range(K):
#     m *= N
#     s *= K-i
#     N -= 1
#
# print(m//s)


# 백준. 11866 요세푸스 문제 0

# N, K = map(int, input().split())
# li = [i+1 for i in range(N)]
# p = -1
#
# print('<', end='')
# for j in range(N):
#     if len(li) != 1:
#         idx = (p+K) % len(li)
#         num = li.pop(idx)
#         print(num, end=', ')
#         p = idx-1
#     else:
#         print(li.pop(p), end='')
#         print('>')


# 백준. 1978 소수 찾기

# N = int(input())
# nums = map(int, input().split())
# check = [i+1 for i in range(1, 1000)]
#
# for j in range(2, 1000):
#     for k in check:
#         if k != j and k % j == 0:
#             check.remove(k)
#
# cnt = 0
# for n in nums:
#     if n in check:
#         cnt += 1
#
# print(cnt)


# 백준. 2775 부녀회장이 될테야

# def plus(d, h, memo):
#     calc = 0
#     if d == 0:
#         return h
#
#     if memo[d][h] != 0:
#         return memo[d][h]
#
#     for i in range(h):
#         calc += plus(d-1, h-i, memo)
#
#     memo[d][h] = calc
#     return calc
#
# T = int(input())
# for t in range(T):
#     k = int(input())
#     n = int(input())
#     memo = [[0] * (n+1) for _ in range(k+1)]
#     print(plus(k, n, memo))
