# 1
# def solution(k, score):
#     answer = []
#     final = []
    
#     for s in score:
#         final.append(s)
#         if len(final) <= k:
#             answer.append(min(final))
#         else:
#             final_ = sorted(final, reverse = True)
#             final_ = final_[:k]
#             answer.append(final_[-1])
    
#     return answer

# 2
import heapq

def solution(k, score):
    answer = []
    final = []
    heapq.heapify(final)
    
    for s in score:
        heapq.heappush(final, s)
        
        if len(final) > k:
            heapq.heappop(final)
        
        answer.append(final[0])
    
    return answer