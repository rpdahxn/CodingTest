import sys
input = sys.stdin.readline

N = input().rstrip()
cnts = [0] * 9  # 0 ~ 8

for n in N:
    n = int(n)
    if n == 9:
        n = 6
    cnts[n] += 1

cnts[6] = (cnts[6]+1) // 2

print(max(cnts))
