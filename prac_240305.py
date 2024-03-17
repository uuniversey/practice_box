
import sys
sys.stdin = open('test.txt')

# 백준. 7579 앱

input = sys.stdin.readline

N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

