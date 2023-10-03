
import sys
sys.stdin = open('test.txt')

# 백준 11650. 좌표 정렬하기

# N = int(input())
# li = []
# for _ in range(N):
#     x, y = map(int, input().split())
#     li.append([x, y])
#
# li.sort()
# for l in li:
#     print(*l)


# 백준 2751. 수 정렬하기 2

# N = int(sys.stdin.readline())
# li = []
# for _ in range(N):
#     n = int(sys.stdin.readline())
#     li.append(n)
# li.sort()
# for l in li:
#     print(l)


# 백준 10866. 덱

# from collections import deque
#
# N = int(input())
# deq = deque()
# for _ in range(N):
#     order = sys.stdin.readline().split()
#     if order[0] == 'push_back':
#         deq.append(int(order[1]))
#     elif order[0] == 'push_front':
#         deq.appendleft(int(order[1]))
#     elif order[0] == 'pop_front':
#         if not deq:
#             print(-1)
#         else:
#             print(deq.popleft())
#     elif order[0] == 'pop_back':
#         if not deq:
#             print(-1)
#         else:
#             print(deq.pop())
#     elif order[0] == 'size':
#         print(len(deq))
#     elif order[0] == 'empty':
#         if not deq:
#             print(1)
#         else:
#             print(0)
#     elif order[0] == 'front':
#         if not deq:
#             print(-1)
#         else:
#             print(deq[0])
#     elif order[0] == 'back':
#         if not deq:
#             print(-1)
#         else:
#             print(deq[-1])


# 백준 10845. 큐

# from collections import deque
#
# N = int(input())
# deq = deque()
# for _ in range(N):
#     order = sys.stdin.readline().split()
#     if order[0] == 'push':
#         deq.append(int(order[1]))
#     elif order[0] == 'pop':
#         if not deq:
#             print(-1)
#         else:
#             print(deq.popleft())
#     elif order[0] == 'size':
#         print(len(deq))
#     elif order[0] == 'empty':
#         if not deq:
#             print(1)
#         else:
#             print(0)
#     elif order[0] == 'front':
#         if not deq:
#             print(-1)
#         else:
#             print(deq[0])
#     elif order[0] == 'back':
#         if not deq:
#             print(-1)
#         else:
#             print(deq[-1])


# 백준 10828. 스택

# from collections import deque
#
# N = int(input())
# deq = deque()
# for _ in range(N):
#     order = sys.stdin.readline().split()
#     if order[0] == 'push':
#         deq.append(int(order[1]))
#     elif order[0] == 'pop':
#         if not deq:
#             print(-1)
#         else:
#             print(deq.pop())
#     elif order[0] == 'size':
#         print(len(deq))
#     elif order[0] == 'empty':
#         if not deq:
#             print(1)
#         else:
#             print(0)
#     elif order[0] == 'top':
#         if not deq:
#             print(-1)
#         else:
#             print(deq[-1])



# 백준 9012. 괄호

# T = int(input())
# for _ in range(T):
#     stack = []
#     li = list(input())
#     for i in li:
#         if i == '(':
#             if stack:
#                 if stack[-1] == i:
#                     stack.append(i)
#             else:
#                 stack.append(i)
#
#         else:
#             if not stack:
#                 print('NO')
#                 break
#             else:
#                 stack.pop()
#     else:
#         if stack:
#             print('NO')
#         else:
#             print('YES')


# 백준 10816. 숫자 카드 2

# N = int(input())
# card = list(map(int, input().split()))
# M = int(input())
# test = list(map(int, input().split()))
#
# check = [0] * 20000001
# for n in card:
#     check[n + 10000000] += 1
#
# for m in test:
#     print(check[m + 10000000], end=' ')


# 백준. 1676 팩토리얼 0의 개수

# N = int(input())
# num = 1
# for i in range(N):
#     num *= (i+1)
#
# for idx, val in enumerate(str(num)[::-1]):
#     if val != '0':
#         print(idx)
#         break


# 백준 7568. 덩치

# N = int(input())
# li = []
#
# for k in range(N):
#     w, h = map(int, input().split())
#     li.append([w, h, 0])
#
# for i in range(N):
#     k = 1
#     for j in li:
#         if li[i][0] < j[0] and li[i][1] < j[1]:
#             k += 1
#     li[i][2] = k
#
# for l in range(N):
#     print(li[l][2], end=' ')


# 백준 10773. 제로

# K = int(input())
# stk = []
# for _ in range(K):
#     k = int(sys.stdin.readline())
#     if k == 0:
#         stk.pop()
#     else:
#         stk.append(k)
# print(sum(stk))


# 백준 11651. 좌표 정렬하기 2

# N = int(input())
# li = []
# for _ in range(N):
#     x, y = map(int, sys.stdin.readline().split())
#     li.append((y, x))
#
# li.sort()
# for l in li:
#     a, b = l
#     print(b, a)


# 백준 18110. solved.ac

# n = int(input())
# li = []
# for _ in range(n):
#     li.append(int(sys.stdin.readline()))
#
# li.sort()
# num = int(n * 0.15 + 0.5)
# for i in range(num):
#     li[i] = 0
#     li[-i-1] = 0
#
# try:
#     print(int(sum(li)/(len(li) - num * 2) + 0.5))
# except ZeroDivisionError:
#     print(0)


# 백준 4949. 균형 잡힌 세상

# while True:
#     flag = 0
#     arr = list(input().rstrip())
#     if arr == ['.']:
#         break
#     stk = []
#     for a in arr:
#         if a == '(' or a == '[':
#             stk.append(a)
#
#         if stk:
#             if a == ')':
#                 if stk[-1] == '(':
#                     stk.pop()
#                 else:
#                     flag = 1
#                     break
#
#             elif a == ']':
#                 if stk[-1] == '[':
#                     stk.pop()
#                 else:
#                     flag = 1
#                     break
#
#         else:
#             if a == ')' or a == ']':
#                 flag = 1
#
#     if not stk:
#         pass
#     else:
#         flag = 1
#
#     if flag:
#         print('no')
#     else:
#         print('yes')


# 백준 1966. 프린터 큐

# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     pri = list(map(int, input().split()))
#     pri[M] -= 0.1
#     save = pri[M]
#
#     print_n = 0
#     while True:
#         p = pri[0]
#         if p == save:
#             if len(pri) == 1:
#                 print(print_n + 1)
#                 break
#             else:
#                 if p == max(pri) or p == max(pri) - 0.1:
#                     print(print_n + 1)
#                     break
#                 else:
#                     pri.pop(0)
#                     pri.append(p)
#
#         elif p == max(pri):
#             pri.pop(0)
#             print_n += 1
#         else:
#             pri.pop(0)
#             pri.append(p)


# 백준 1874. 스택 수열

# n = int(input())
# nums = [i+1 for i in range(n)]
# arr = []
# for _ in range(n):
#     arr.append(int(sys.stdin.readline()))
#
# std = []
# res = []
# stk = []
# k = 0
# num = 1
# while num <= n:
#     if not stk:
#         stk.append(num)
#         res.append('+')
#     else:
#         if arr[k] != stk[-1]:
#             stk.append(num)
#             res.append('+')
#         else:
#             res.append('-')
#             std.append(stk.pop())
#             k += 1
#             num -= 1
#     num += 1
#
# while stk:
#     std.append(stk.pop())
#     res.append('-')
#
# if std == arr:
#     for r in res:
#         print(r)
#
# else:
#     print('NO')


