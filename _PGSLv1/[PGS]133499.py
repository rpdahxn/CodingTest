# 1
# def solution(babbling):
#     answer = 0
#     nephew = ["aya", "ye", "woo", "ma"]
    
#     for b in babbling:
#         b_ = b
#         temp = []
#         while b_:
#             if b_[:3] in nephew and b_[:3] != temp:
#                 temp = b_[:3]
#                 b_ = b_[3:]
#             elif b_[:2] in nephew and b_[:2] != temp:
#                 temp = b_[:2]
#                 b_ = b_[2:]
#             else:
#                 break
                
#         if not b_:
#             answer += 1
            
    
#     return answer

# 2
def solution(babbling):
    answer = 0
    nephew = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        for i in range(4):
            if nephew[i]*2 in b:
                break
            else:
                b = b.replace(nephew[i], " ")
        if len(b.strip()) == 0:
            answer += 1
            
    return answer