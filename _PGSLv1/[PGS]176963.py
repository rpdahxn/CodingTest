def solution(name, yearning, photo):
    answer = []
    dict_ = {n:y for n, y in zip(name, yearning)}
    
    for p in photo:
        sum_ = 0
        for i in p:
            if i in dict_.keys():
               sum_ += dict_[i]
        answer.append(sum_)
            
    
    return answer