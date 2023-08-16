def solution(s):
    answer = 0
    s = list(s)
    
    cnt1 = 1
    c = s[0]
    cnt2 = 0
    
    for i in range(1, len(s)):
        if c == '*':
            c = s[i]
            cnt1 = 1
            cnt2 = 0
            continue
            
        if s[i] == c:
            cnt1 += 1
        else:
            cnt2 += 1
        
        if cnt1 == cnt2:
            c = '*'
            answer += 1
            
    return answer if c == '*' else answer+1