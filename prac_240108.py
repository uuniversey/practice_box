import sys
sys.stdin = open('test.txt')


def dfs(k, num, parent):
    for j in adj_l[k]:
        if not vstd[j]:
            vstd[j] = num
            dfs(j, num, k)

while True:
    n, m = map(int, input().split())
    if not n + m:
        break

    adj_l = [[] for _ in range(n + 1)]

    for i in range(m):
        a, b = map(int, input().split())
        adj_l[a].append(b)
        adj_l[b].append(a)

    vstd = [0] * (n+1)
    istree = [0] * (n+1)
    num = 1
    for k in range(1, n+1):
        dfs(k, num, 0)
        num += 1

    vstd.pop(0)
    istree.pop(0)
    zero = vstd.count(0)
    one = vstd.count(1)
    print(vstd)
    print(istree)

    if one == n:
        print(f'Case 2: there is one trees.')
    elif zero + one == n:
        print(f'Case 1: A forest of {1 + zero} tree.')
    else:
        print(f'Case 3: No trees.')
