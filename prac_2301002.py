
import sys
sys.stdin = open('test.txt')

# 백준 1259. 팰린드롬수

# while True:
#     s = input()
#     if s == '0':
#         break
#     s_r = s[::-1]
#     print('yes' if s == s_r else 'no')


# 백준 1920. 수 찾기

# N = int(input())
# A = set(input().split())
# M = int(input())
# M_A = input().split()
# num = len(A)
#
# for m in M_A:
#     A.add(m)
#
#     if len(A) != num:
#         print('0')
#         A.remove(m)
#     else:
#         print('1')


# 백준 2164. 카드2

# from collections import deque
#
# N = int(input())
# card = deque(i+1 for i in range(N))
# for _ in range(N-1):
#     card.popleft()
#     recy = card.popleft()
#     card.append(recy)
# print(card[0])


# 백준 2609. 최대공약수와 최소공배수

# N, M = map(int, input().split())
# n = min(N, M)
# x = 0
# for i in [j+1 for j in range(n)]:
#     if N % i == 0 and M % i == 0:
#         x = i
#
# print(x)
# print(N//x * M//x * x)


# 백준. 10814. 나이순 정렬

# N = int(input())
# li = []
# num = 0
# for _ in range(N):
#     age, name = input().split()
#     li.append((int(age), num, name))
#     num += 1
# li.sort()
#
# for l in li:
#     print(int(l[0]), l[2])