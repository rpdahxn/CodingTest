def solution(plans):
    answer = []
    stopped = []
    
    for i in range(len(plans)):
        hour, minute = list(map(int, plans[i][1].split(":")))
        plans[i][1] = hour*60 + minute
        plans[i][2] = int(plans[i][2])
    # 시간순으로 정렬
    plans.sort(key = lambda x : x[1])
    
    for i in range(len(plans)):
        if i == len(plans)-1:
            answer.append(plans[i][0])
            while stopped:
                answer.append(stopped.pop(-1)[0])
            return answer
        
        cur_t = plans[i][1] + plans[i][2]
        
        if cur_t == plans[i+1][1]:
            answer.append(plans[i][0])
        # 과제 완료시 시간이 초과되는 경우
        elif cur_t > plans[i+1][1]:
            stopped.append([plans[i][0], cur_t - plans[i+1][1]])
            # 현재 시간 다시 수정
            cur_t = plans[i+1][1]
        # 과제 완료 후 시간이 남는 경우
        elif cur_t < plans[i+1][1]:
            answer.append(plans[i][0])
            while stopped:
                name, playtime = stopped.pop(-1)
                cur_t += playtime
                if cur_t == plans[i+1][1]:
                    answer.append(name)
                    break
                elif cur_t < plans[i+1][1]:
                    answer.append(name)
                elif cur_t > plans[i+1][1]:
                    stopped.append([name, cur_t - plans[i+1][1]])
                    cur_t = plans[i+1][1]
                    break