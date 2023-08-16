def solution(today, terms, privacies):
    answer = []
    # 모든 달은 28일까지
    terms_ = {}
    for t in terms:
        c, m = t.split(" ")
        terms_[c] = int(m)
        ㅜ
    y, m, d = map(int, today.split("."))
    today_ = y * 12 * 28 + m * 28 + d
    
    for i, p in enumerate(privacies):
        date, c = p.split(" ")
        y, m, d = map(int, date.split("."))
        
        # 모두 '일' 단위로 바꾸기
        date_ = y * 12 * 28 + m * 28 + d
        date_ += 28 * terms_[c]

        if date_-1 < today_:
            answer.append(i+1)
    
    return answer