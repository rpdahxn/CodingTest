def solution(picks, minerals):
    answer = 0
    end = min(sum(picks)*5, len(minerals))
    
    minerals_to_num = []
    # 광물들 5개 단위로 자르기
    for i in range(0, end, 5):
        if i+5 > end:
            minerals_ = minerals[i:]
        else:
            minerals_ = minerals[i:i+5]
        d, i, s = minerals_.count("diamond"), minerals_.count("iron"), minerals_.count("stone")
        minerals_to_num.append([d, i, s])
        
    minerals_to_num.sort(key = lambda x : (-x[0], -x[1]))
    
    for m in (minerals_to_num):
        if picks[0] > 0:
            picks[0] -= 1
            answer += sum(m)
        elif picks[1] > 0:
            picks[1] -= 1
            answer += (m[0]*5 + m[1]*1 + m[2]*1)
        else:
            picks[2] -= 1
            answer += (m[0]*25 + m[1]*5 + m[2]*1)
            
    return answer
            