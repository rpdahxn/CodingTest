def solution(keymap, targets):
    answer = [0] * len(targets)
    
    for i in range(len(targets)):
        for t in targets[i]:
            idx = [k.index(t)+1 for k in keymap if t in k]
            if not idx:
                answer[i] = -1
                break
            else:
                answer[i] += min(idx)

    return answer