
# 백준 9205. 맥주 마시면서 걸어가기

import sys
sys.stdin = open('test.txt')


def dfs(s):
    global ans
    if s == n+1:
        ans = 'happy'
        return

    vstd[s] = 1
    mx, my = market[s]
    for idx, val in enumerate(market):
        x, y = val
        # 거리 재서 갈 수 있는 거리면 (1000) 거기로 가기
        if vstd[idx] == 0 and abs(x - mx) + abs(y - my) <= 1000:
            vstd[idx] = 1
            dfs(idx)


input = sys.stdin.readline
t = int(input())
# 출발점이랑 도착점까지 다 모아놓음
for _ in range(t):
    n = int(input())
    market = (
                [list(map(int, input().split()))] +
                [list(map(int, input().split())) for _ in range(n)] +
                [list(map(int, input().split()))]
              )
    # 그래서 n+2 임
    vstd = [0] * (n+2)
    ans = 'sad'
    dfs(0)
    print(ans)