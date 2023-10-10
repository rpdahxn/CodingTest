from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[-1]*(51*2) for _ in range(51*2)]
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if x1 < x < x2 and y1 < y < y2:
                    graph[x][y] = 0
                elif graph[x][y] != 0:
                    graph[x][y] = 1
        
        
    def bfs(characterX, characterY):
        visited = [[1]*(51*2) for _ in range(51*2)]
        queue = deque()
        queue.append([characterX, characterY])
        
        move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        while queue:
            x, y = queue.popleft()
            
            if x == itemX * 2 and y == itemY * 2:
                return visited[x][y] // 2
            
            for m in move:
                nx, ny = x + m[0], y + m[1]
                if graph[nx][ny] == 1 and visited[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y]+1
                    queue.append([nx, ny])
    
    return bfs(characterX*2, characterY*2)