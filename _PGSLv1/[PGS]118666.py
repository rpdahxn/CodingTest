def solution(survey, choices):
    answer = ''
    dic = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    
    for s, c in zip(survey, choices):
        score = [3, 2, 1, 0, 1, 2, 3]
        
        if c > 3:
            dic[s[1]] += score[c-1]
        else:
            dic[s[0]] += score[c-1]
    
    if dic["R"] >= dic["T"]:
        answer += "R"
    else:
        answer += "T"
    if dic["C"] >= dic["F"]:
        answer += "C"
    else:
        answer += "F"
    if dic["J"] >= dic["M"]:
        answer += "J"
    else:
        answer += "M"
    if dic["A"] >= dic["N"]:
        answer += "A"
    else:
        answer += "N"
        
    return answer