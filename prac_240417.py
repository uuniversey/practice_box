import sys
sys.stdin = open('test.txt')

# 백준. 13904 과제
import heapq

input = sys.stdin.readline
N = int(input())
hq = []
memo = 0

for _ in range(N):
    D, W = list(map(int, input().split()))
    heapq.heappush(hq, (-W, D))     # 점수를 기준으로 가장 큰 값부터 나오게 힙 구성
    memo = max(memo, D)             # 최대 마감일을 기록

check = [0] * (memo+1)              # 값이 들어 있는지 확인하기 위한 리스트
ans = 0
while hq:
    point, day = heapq.heappop(hq)
    point = -point                  # 점수를 양수로 되돌려줌

    for i in range(day, 0, -1):     # 체크가 안되어 있는 부분(비어있는 부분)에 점수를 채워 넣음
        if not check[i]:
            check[i] = 1
            ans += point
            break

print(ans)