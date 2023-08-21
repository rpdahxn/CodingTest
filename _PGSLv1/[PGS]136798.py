def divisor(n):
    cnt = 0
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            cnt += 1
            if i*i != n:
                cnt += 1
    return cnt

def solution(number, limit, power):
    answer = 0
    number_ = []
    
    for n in range(number):
        temp = divisor(n+1)
        
        if temp > limit:
            answer += power
        else:
            answer += temp
    
    return answer