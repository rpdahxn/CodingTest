def solution(sequence, k):
    min_ = 1000001
    l = len(sequence)
    start = end = 0
    sum_ = 0
    answer = []
    
    for start in range(l):
        while end < l and sum_ < k:
            sum_ += sequence[end]
            end+=1

        if sum_ == k and end-start < min_:
            min_ = end-start
            answer = [start, end-1]
        sum_ -= sequence[start]
    
    return answer