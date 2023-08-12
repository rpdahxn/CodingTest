def solution(n, m, section):
    answer = 0
    colored = [False] * n
    for s in section:
        if not colored[s-1]:
            answer += 1
            colored[s-1:s-1+m] = [True] * m
    
    return answer