
import sys
sys.stdin = open('test.txt')

# 백준 1010. 다리 놓기

# import math
# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     ans = math.comb(M, N)
#     print(ans)



# 백준 1015. 수열 정렬

# N = int(input())
# arr_A = list(map(int, input().split()))
# arr_B = list(map(int, input().split()))
# arr_A.sort(reverse=True)
# arr_B.sort()
#
# S = 0
# for idx, val in enumerate(arr_A):
#     S += val * arr_B[idx]
# print(S)