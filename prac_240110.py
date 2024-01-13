
import sys
sys.stdin = open('test.txt')

# 백준 1833. 고속철도 설계하기

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    parent[max(x, y)] = min(x, y)


N = int(input())
adj_l = [list(map(int, input().split())) for _ in range(N)]
C = 0
M = 0
parent = [_ for _ in range(N+1)]
link_info = []
cost_info = []
n = 0
# 받은 input을 통해서 간선 정보를 만들어 준다.
for li in adj_l:
    n += 1
    for m in range(n-1, N):
        # 비용이 음수라면 이미 고속도로가 설치되어 있는 애들이고 걔내를 link_info에 담는다 (비용, 간선 좌표)
        if li[m] < 0:
            link_info.append([-li[m], n, m+1])
        # 0이 아닌 양수라면 cost_info에 담는다 (비용, 간선 좌표)
        else:
            if li[m] != 0:
                cost_info.append([li[m], n, m+1])

# 먼저 연결 되어 있는 애들을 합쳐서 비용 계산을 해놓음
for c, x, y in link_info:
    union(x, y)
    C += c

# 연결이 안되어 있는 cost_info에 있는 친구들을 계산하기 위해 kruskal 알고리즘을 사용할 것이므로 비용을 낮은 순으로 정렬
cost_info.sort()
# 마지막 도시 번호 출력을 위한 리스트
record = []
for c, x, y in cost_info:
    # kruskal 알고리즘 즉, 싸이클이 아니라면 합치고 비용을 계산하고 추가된 고속도로 갯수를 더해주고 record에 도시 번호를 담는다.
    if find(x) != find(y):
        union(x, y)
        C += c
        M += 1
        record.append([x, y])

print(C, M)
for a, b in record:
    print(a, b)