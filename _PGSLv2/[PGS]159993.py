from collections import deque

def solution(maps):
    # 출발 -> 레버를 거쳐 -> 문을 찾아야 함
    answer = []
    
    h = len(maps)
    w = len(maps[0])
    
    def bfs(S, E):
        for i in range(h):
            if S in maps[i]:
                start_x, start_y = i, maps[i].index(S)
        
        visited = [[-1] * w for _ in range(h)]
        visited[start_x][start_y] = 0
        
        queue = deque()
        queue.append([start_x, start_y])
        
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        while queue:
            x, y = queue.popleft()
            
            for move in moves:
                nx, ny = x + move[0], y + move[1]
                if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == -1 and maps[nx][ny] != 'X':
                    if maps[nx][ny] == E:
                        return visited[x][y]+1
                        
                    visited[nx][ny] = visited[x][y]+1
                    queue.append([nx, ny])
        return -1
    
    answer.append(bfs('S', 'L'))
    answer.append(bfs('L', 'E'))
    return -1 if -1 in answer else sum(answer)