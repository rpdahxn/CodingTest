def solution(a, b, n):
    answer = 0
    if a > n:
        return answer
    
    while n >= a:
        divisor = n // a
        left = n % a
        
        n = divisor*b + left
        answer += divisor*b
    
    return answer