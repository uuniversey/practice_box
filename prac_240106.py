# 백준. 20055 컨베이어 벨트 위의 로봇

import sys
sys.stdin = open('test.txt')

from collections import deque

N, K = map(int, input().split())
Belt = list(map(int, input().split()))
Belt = deque(Belt)

result = 1
robots = deque([0] * N)
while True:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    Belt.rotate(1)
    robots.rotate(1)
    robots[N-1] = 0

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면
    # 이동한다. 만약 이동할 수 없다면(이동하려는 칸에 로봇이 있거나 칸 내구도가 없다면) 가만히 있는다.
    for i in range(N-2, -1, -1):
        if robots[i] and robots[i+1] == 0 and Belt[i+1]:
            robots[i] = 0
            robots[i+1] = 1
            Belt[i+1] -= 1
    robots[N-1] = 0

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if Belt[0] != 0:
        robots[0] = 1
        Belt[0] -= 1

    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    num = Belt.count(0)
    if num >= K:
        break
    else:
        result += 1

print(result)

