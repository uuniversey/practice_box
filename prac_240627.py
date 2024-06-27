import sys
sys.stdin = open('test.txt')

# 백준 30802. 웰컴 키트

# N = int(input())
# size = list(map(int, input().split()))
# T, P = map(int, input().split())
#
# t = 0
# for s in size:
#     if s != 0:
#         if s%T:
#             t += (s//T + 1)
#         else:
#             t += s//T
#
# print(t)
# print(N//P, N%P)



# 백준 28702. FizzBuzz

# strs = [input() for _ in range(3)]
#
# for idx, val in enumerate(strs):
#     try:
#         num = int(val)
#     except ValueError:
#         continue
#
#     if idx == 0:
#         ans = num + 3
#         break
#     elif idx == 1:
#         ans = num + 2
#         break
#     else:
#         ans = num + 1
#         break
#
# if ans % 3:
#     if ans % 5:
#         print(ans)
#     else:
#         print('Buzz')
# else:
#     if ans % 5:
#         print('Fizz')
#     else:
#         print('FizzBuzz')



# 백준 31403. A+B-C

# strs = [input() for _ in range(3)]
# print(int(strs[0])+int(strs[1])-int(strs[2]))
# print(int(strs[0]+strs[1])-int(strs[2]))



# 백준 2805. 나무 자르기

# def bs(s, e):
#     global ans
#     if s > e:
#         return
#     calc = 0
#     m = (s+e)//2
#     for h in highs:
#         if h >= m:
#             calc += h - m
#     if calc < M:
#         bs(s, m-1)
#     else:
#         ans = m
#         bs(m+1, e)
#
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# highs = list(map(int, input().split()))
# highs.sort()
# ans = 0
# bs(1, highs[-1])
# print(ans)