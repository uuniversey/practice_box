
import sys
sys.stdin = open('test.txt')

# 백준 1253. 좋다

# # 찾아야 하는 target, 처음부터 움직이는 포인터, 마지막부터 움직이는 포인터
# def tp(t, s, e):
#     # 예외처리: 다른 수 두 개의 합으로 나타낼 수 있어야 하므로 자기 자신 포함 안되게
#     while(s < e):
#         if s == t:
#             s += 1
#             continue
#         elif e == t:
#             e -= 1
#             continue
#
#         if arr[s]+arr[e] < arr[t]:
#             s += 1
#         elif arr[s]+arr[e] > arr[t]:
#             e -= 1
#         else:
#             return True
#
# N = int(input())
# arr = sorted(list(map(int, input().split())))
# ans = 0
#
# for i in range(N):
#     if tp(i, 0, N-1):
#         ans += 1
#
# print(ans)



# 백준 2457. 공주님의 정원

input = sys.stdin.readline
N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
info.sort(key=lambda x: (-x[2], -x[3]))
print(info)

memo = 1231
cand = []
flag = 1
for idx, val in enumerate(info):
    m1, d1, m2, d2 = val
    if flag:
        if 100*m2 + d2 >= 1201:
            if memo > 100*m1 + d1:
                memo = 100*m1 + d1

        else:
            cand.append(idx - 1)
            flag = 0

    else:
        if 100 * m2 + d2 >= memo:
            if memo > 100 * m1 + d1:
                memo = 100 * m1 + d1
                cand.append(idx - 1)


print(cand)