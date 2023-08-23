def solution(X, Y):
    X = list(X)
    Y = list(Y)
    numbers = []
    
    inter = set(X).intersection(set(Y))
    if not inter:
        return "-1"
    
    for i in inter:
        cnt = min(X.count(i), Y.count(i))
        for _ in range(cnt):
            numbers.append(int(i))
    
    if sum(numbers) == 0:
        return "0"
    
    numbers.sort(reverse = True)      
    return ''.join([str(_) for _ in numbers])