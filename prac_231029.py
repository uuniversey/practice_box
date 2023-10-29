
import sys
sys.stdin = open('test.txt')

# 백준. 5972 택배 배송
import heapq

N, M = map(int, input().split())
adj_l = [[] for _ in range(N+1)]
vt = [float('inf')] * (N+1)
for _ in range(M):      # 인접리스트 생성 ( 양방향 )
    A, B, C = map(int, input().split())
    adj_l[A].append((C, B))
    adj_l[B].append((C, A))

vt[1] = 0       # 첫
hq = [(0, 1)]   # 시작 (소의 수, 노드 위치)
while hq:
    val, position = heapq.heappop(hq)
    for v, p in adj_l[position]:
        if vt[p] > vt[position] + v:    # 다음 방문할 vt가 더 큰 값이면 갱신
            vt[p] = vt[position] + v
            heapq.heappush(hq, (vt[p], p))    # 갱신을 했을 때만 푸쉬 (안 그러면 무한 루프)

print(vt[N])