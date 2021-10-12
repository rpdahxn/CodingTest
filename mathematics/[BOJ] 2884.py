# 내 코드
# H, M = map(int, input().split())

# if M >= 45:
#     M -= 45
#     print("%d %d" % (H, M))
# else:
#     M = 60 + (M - 45)
#     H -= 1
#     if H < 0:
#         H += 24
#     print("%d %d" % (H, M))

H, M = map(int, input().split())
M = M + (H*60) - 45
print("%d %d" % (M//60 % 24, M % 60))
