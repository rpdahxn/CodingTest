# 내코드
# 소수를 구해야 한다고 생각했다..

# def isPrime(n):
#     count=0
#     for i in range(1, n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#         return True
#     else:
#         return False

# n = int(input())
# 약수
#

# 정답코드
N = int(input())
m = 2
while N != 1:
    if N % m == 0:
        print(m)
        N = N // m
    else:
        m += 1
