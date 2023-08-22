def solution(ingredient):
    answer = 0
    # 1 2 3 1 순서대로
    
    burger = [1,2,3,1]
    temp = []
    for ig in (ingredient):
        temp.append(ig)
        if temp[-4:] == burger:
            for _ in range(4):
                temp.pop()
            answer += 1

    return answer