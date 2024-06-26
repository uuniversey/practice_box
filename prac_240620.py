
import sys
sys.stdin = open('test.txt')


# 백준 1431. 시리얼 번호

# N = int(input())
# codes = []
# dic = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
# for _ in range(N):
#     code = input()
#     num = 0
#     for c in code:
#         if c in dic:
#             num += int(c)
#     codes.append((len(code), num, code))
#
# codes.sort()
# for cd in codes:
#     print(cd[2])


# 백준 22864. 피로도

# A, B, C, M = map(int, input().split())
# battery, time, work = 0, 0, 0
# while time <= 23:
#     if A + battery > M:
#         battery = max(battery-C, 0)
#     else:
#         battery += A
#         work += B
#     time += 1
# print(work)