

import sys
sys.stdin = open('test.txt')


# 백준 1141. 접두사

# N = int(input())
# words = [input() for _ in range(N)]
# words.sort()
# res = []
#
# for i in range(N-1):
#     # a.startswith(b) => b가 a의 접두사니? true/false
#     if words[i+1].startswith(words[i]):
#         continue
#     res.append(words[i])
#
# print(len(res)+1)


# 백준 2473. 세 용액

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# min_v = sys.maxsize
# ans = []
#
# for i in range(N-2):
#     left, right = i+1, N-1
#     while left < right:
#         val = arr[i] + arr[left] + arr[right]
#         if min_v > abs(val):
#             min_v = abs(val)
#             ans = [arr[i], arr[left], arr[right]]
#
#         if val < 0:
#             left += 1
#         elif val > 0:
#             right -= 1
#         else:
#             break
# print(*ans)



# 백준 1202. 보석 도둑

input = sys.stdin.readline
N, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
info.sort(key=lambda x:-x[1])
bags = sorted([int(input()) for _ in range(K)])

ans = [0] * K
memo = ''
for idx, val in enumerate(bags):
    for i, v in enumerate(info):
        if memo == v:
            continue
        M, V = v
        if M <= val:
            if ans[idx] < V:
                ans[idx] = V
                memo = v

print(sum(ans))