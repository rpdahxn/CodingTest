import sys
input = sys.stdin.readline

n = int(input())

children = [int(input()) for _ in range(n)]
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if children[j] < children[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))