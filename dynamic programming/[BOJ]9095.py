import sys
input = sys.stdin.readline

T = int(input())

n_list = []

for _ in range(T):
    n_list.append(int(input()))

dp = [0]*(max(n_list)+1)
# 1을 만드는 방법의 수 : 1 => 1
dp[1] = 1

# 2를 만드는 방법의 수 : 1+1, 2 => 2
dp[2] = 2

# 3을 만드는 방법의 수 : 1+1+1, *1+2, 2+1, *3 => 4
dp[3] = 4

for i in range(4, len(dp)):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

for n in n_list:
    print(dp[n])