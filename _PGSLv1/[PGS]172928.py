def solution(park, routes):
    answer = []
    dic = {'E':[0, 1], 'S':[1, 0], 'W':[0, -1], 'N':[-1, 0]}
    
    for i in range(len(park)):
        if 'S' in park[i]:
            x = i
            y = park[i].index('S')
    
    for r in routes:
        dir, dist = r.split(" ")
        dist = int(dist)
        move = dic[dir]
        
        temp_x = dist*move[0]+x
        temp_y = dist*move[1]+y
        # 우선 공원 밖을 나가지 않는다면
        if (temp_x >= 0 and temp_x < len(park)) and (temp_y >= 0 and temp_y < len(park[0])):       
            isX = False
            for i in range(1, dist+1):
                if park[x+move[0]*i][y+move[1]*i] == 'X':
                    isX = True
                    break
                    
            if not isX:
                x = temp_x
                y = temp_y
                    
    return [x, y]