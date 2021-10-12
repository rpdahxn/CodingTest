print("입력해라")
N = int(input())
count = 0

while True:
    if N%3 == 0:
        N /= 3
        count += 1
    elif N%2 == 0 and N != 2:
        N /= 2
        count += 1
    else:
        N -= 1
        count += 1 

    print("숫자랑 카운트 : %d %d" %(N, count))
    if N == 1:
        break
    

print(count)