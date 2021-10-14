# 내 코드

# a, b = map(int, input().split())

# if (a > b):
#     big = a
#     small = b
# else:
#     big = b
#     small = a
# gcd = 1
# for i in range(1, small+1):
#     if (big % i == 0) and (small % i == 0):
#         gcd = i

# print("%d\n%d" % (gcd, gcd * (big//gcd) * (small//gcd)))

# 정답 코드
# 유클리드 호제법
# def gcd(x, y):
#     if y != 0:
#         return gcd(y, x % y)
#     else:
#         return x


# def lcm(x, y):
#     return (x*y)//gcd(x, y)


# N, M = map(int, input().split())

# print(gcd(N, M))
# print(lcm(N, M))

# 다시 풀기
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))
