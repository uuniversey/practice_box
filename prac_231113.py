
import sys
sys.stdin = open('test.txt')

N, M = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

# 첫번째 행 - 무조건 오른쪽으로
for j in range(1, M):
    ground[0][j] += ground[0][j-1]

# 그 다음 행 부터는 왼쪽에서 오른쪽으로 가는거, 오른쪽에서 왼쪽으로 가는거 둘중 최댓값을 선정해야 함
for r in range(1, N):
    left = [ground[r][c] + ground[r-1][c] for c in range(M)]
    right = [ground[r][c] + ground[r-1][c] for c in range(M)]

    print(left, right)

    # 왼 -> 오
    for c in range(1, M):
        left[c] = max(left[c], left[c-1] + ground[r][c])

    # 오 <- 왼
    for c in range(M-2, -1, -1):
        right[c] = max(right[c], right[c+1] + ground[r][c])

    for c in range(M):
        ground[r][c] = max(left[c], right[c])

print(ground[N-1][M-1])