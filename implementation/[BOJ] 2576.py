sum = 0
min = 100

for i in range (7):
    num = int(input())
    if (num % 2 != 0):
        sum += num
        if (num < min):
            min = num

if (min==100):
    print(-1)
else:
    print("%d\n%d" %(sum , min))