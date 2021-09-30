def solution(participant, completion):
    for p in participant:
        f=0
        for c in completion:
            if p==c:
                f=1
                completion.remove(c)
        if f==0:
            break
    answer = p
    return answer