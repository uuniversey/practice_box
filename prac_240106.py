# 백준. 20055 컨베이어 벨트 위의 로봇

import sys
sys.stdin = open('test.txt')

# from collections import deque
#
# N, K = map(int, input().split())
# Belt = list(map(int, input().split()))
# Belt = deque(Belt)
#
# result = 1
# robots = deque([])
# while True:
#     # 1
#     tmp = Belt.pop()
#     Belt.appendleft(tmp)
#     for robot in robots:
#         if robot[1] != 0:
#             robot[0] += 1
#             if robot[0] == N-1:
#                 robot[1] = 0
#
#     # 2
#     if robots:
#         for i in range(len(robots)):
#             if robots[i][1] == 1:
#                 if Belt[robots[i][0] + 1] != 0:
#                     Belt[robots[i][0] + 1] -= 1
#                     robots[i][0] += 1
#                     if robots[i][0] == N-1:
#                         robots[i][1] = 0
#
#     # 3
#     if Belt[0] != 0:
#         robots.append([0, 1])
#         Belt[0] -= 1
#
#     # 4
#     num = Belt.count(0)
#     if num >= K:
#         break
#     else:
#         print(result, Belt)
#         result += 1
#
# print(result)


from collections import deque

N, K = map(int, input().split())
Belt = list(map(int, input().split()))
Belt = deque(Belt)

result = 1
robots = deque([0] * N)

while True:
    # 1
    Belt.rotate(1)
    robots.rotate(1)
    robots[N-1] = 0  # 로봇이 벨트 끝에 도달하면 제거

    # 2
    for i in range(N-2, -1, -1):
        if robots[i] == 1 and robots[i+1] == 0 and Belt[i+1] > 0:
            robots[i] = 0
            robots[i+1] = 1
            Belt[i+1] -= 1
    robots[N-1] = 0  # 로봇이 벨트 끝에 도달하면 제거

    # 3
    if robots[0] == 0 and Belt[0] > 0:
        robots[0] = 1
        Belt[0] -= 1

    # 4
    if Belt.count(0) >= K:
        break
    result += 1

print(result)

