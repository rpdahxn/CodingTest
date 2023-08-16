# 1
# def solution(s):
#     answer = []
    
#     for i, _ in enumerate(s):
#         if i == 0 or _  not in s[:i]:
#             answer.append(-1)
#         else:
#             tmp = i
#             while 1:
#                 tmp -= 1
#                 if s[tmp] == _:
#                     break
#             answer.append(i-tmp)
    
#     return answer

# 2
def solution(s):
    answer = []
    dic = {}
    
    for i, _ in enumerate(s):
        if i == 0 or _  not in dic.keys():
            answer.append(-1)
        else:
            answer.append(i-dic[_])
        
        # 인덱스 값 갱신
        dic[_] = i
    
    return answer