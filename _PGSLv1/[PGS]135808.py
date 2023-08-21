def solution(k, m, score):
    answer = 0
    boxes = len(score)//m
    
    score.sort()
    if boxes > 0:
        for i in range(boxes):
            answer += score[-m*(i+1)]*m
    else:
        answer = 0
    
    return answer