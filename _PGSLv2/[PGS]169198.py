import math
def dist(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2

def solution(m, n, startX, startY, balls):
    answer = []
    
    for (x, y) in balls:
        dists = []
        
        # 위
        if not (startX == x and y >= startY):
            y_ = n + (n - y)
            dists.append(dist(startX, startY, x, y_))
        # 아래
        if not (startX == x and y < startY):
            y_ = -y
            dists.append(dist(startX, startY, x, y_))
        # 왼
        if not (startY == y and x <= startX):
            x_ = -x
            dists.append(dist(startX, startY, x_, y))
        # 오
        if not (startY == y and x > startX):
            x_ = m + (m - x)
            dists.append(dist(startX, startY, x_, y))
        answer.append(min(dists))
            
    return answer