n, k = map(int, input().split())
money = []
count = 0

for _ in range(n):
    money.append(int(input()))

for i in range(1, n+1):
    q = k // money[n-i]
    k -= q * money[n-i]
    count += q
    if k == 0:
        break

print(count)
