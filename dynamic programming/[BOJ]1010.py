import sys, math
input = sys.stdin.readline

T = int(input())
sum_ = 0

for _ in range(T):
    N, M = map(int, input().split())
    res = math.factorial(M) // (math.factorial(N) * math.factorial(M-N))
    print(res)
