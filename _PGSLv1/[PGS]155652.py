# 1
# def solution(s, skip, index):
#     answer = ''
#     alphabet = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    
#     for _ in s:
#         idx = alphabet.index(_)+index
#         if idx >= len(alphabet):
#             idx %= len(alphabet)
#         answer+=alphabet[idx]
    
#     return answer

# 2
def solution(s, skip, index):
    alphabet = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    
    return "".join([alphabet[(alphabet.index(_)+index) % len(alphabet)] for _ in s])