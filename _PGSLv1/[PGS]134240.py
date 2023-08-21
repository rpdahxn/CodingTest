def solution(food):
    start = []
    end = []
    for i, f in enumerate(food):
        if i == 0:
            continue
        tmp = f // 2
        if tmp >= 1:
            start.append(str(i)*tmp)
            end.insert(0, str(i)*tmp)
    
    return ''.join(start)+'0'+''.join(end)