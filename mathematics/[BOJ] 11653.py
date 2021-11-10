# 정답 1
# N = int(input())
# m = 2
# while N != 1:
#     if N % m == 0:
#         print(m)
#         N = N // m
#     else:
#         m += 1

# 정답 2
n = int(input())
i = 2
r = int(n ** 0.5)

while i <= r:
    while not n % i:
        print(i)
        n //= i
    i += 1
if n > 1:
    print(n)

# 내 코드
# N = int(input())
# m = 2
# while True:
#     if N % m == 0:
#         N //= m
#         print(m)
#         if N == 1:
#             break
#     else:
#         m += 1
