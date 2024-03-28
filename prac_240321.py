import sys
sys.stdin = open('test.txt')

# 백준. 1300 K번째 수


N = int(input())
k = int(input())

s, e = 1, k
while s <= e:
    mid = (s+e) // 2
    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid//i, N)

    if cnt >= k:
        res = mid
        e = mid - 1
    else:
        s = mid + 1

print(res)
