N = int(input())
time = list(map(int, input().split()))
time.sort()
total = 0

# for i in range(N):
#     total += sum(time[:i+1])

for i in range(1, N):
    time[i] += time[i-1]

# print(total)
print(sum(time))