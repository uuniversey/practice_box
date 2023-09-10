

# 백준. 10157 자리 배정

# import sys
# sys.stdin = open('wj.txt', 'r')
#
# N, K = map(int, input().split())
# room = [[0] * 6 for _ in range(2)]      # 학생들 분류
# result = 0
#
# for i in range(N):
#     s, y = map(int, input().split())
#     room[s][y-1] += 1           # 학생들을 각 조건에 따라 나눠 준다.
#
# for j in range(2):
#     for k in range(6):
#         if room[j][k] > K:      # 학생의 수가 제한된 인원 수보다 많다면
#             result += (room[j][k] // K)     # 몫만큼 더해주고
#             if room[j][k] % K:      # 나머지가 있다면 방이 더 필요하므로 1을 더 더해준다.
#                 result += 1
#         elif 0 < room[j][k] <= K:
#             result += 1         # 제한된 인원 수보다 적다면 방 한개 추가해 준다.
#
# print(result)





# 백준. 11950  2016 ioi

import sys
sys.stdin = open('wj.txt', 'r')



N, M = map(int,input().split())
arr = [input() for _ in range(N)]

max_v = 0
for i in range(N-2):  # 흰색 영역 인덱스 설정
    for j in range(i+1, N-1):  # 파랑색 영역 인덱스 설정 그리고 나머지는 빨강영역이다.
        cnt = 0
        for s in range(i+1):           #하얀 영역
            cnt += arr[s].count('W') # W의 개수를 세라
        for s in range(i+1, j+1):      # 파란 영역
            cnt += arr[s].count('B') # B의 개수를 세라
        for s in range(j+1, N):        # 빨간 영역
            cnt += arr[s].count('R') # R의 개수를 세라
        max_v = max(max_v, cnt)

print(N*M -max_v)
