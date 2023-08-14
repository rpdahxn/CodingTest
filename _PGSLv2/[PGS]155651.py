def to_min(time):
    h = int(time[:2])
    m = int(time[-2:])
    return 60*h+m

def solution(book_time):
    answer = 0
    book_time_ = [[to_min(time1), to_min(time2)+10] for time1, time2 in book_time]
    book_time_.sort(key = lambda x: (x[0], x[1]))
    rooms = [[0] * (1440) for _ in range(len(book_time_))]
    
    # 0 부터 -> 24시*60= =1440까지
    for t1, t2 in book_time_:
        for room in rooms:
            if sum(room[t1+1:t2-1]) == 0:
                room[t1:t2+1] = [1] * (t2-t1+1)
                break
                
    for room in rooms:
        if sum(room) != 0:
            answer += 1
            
    return answer