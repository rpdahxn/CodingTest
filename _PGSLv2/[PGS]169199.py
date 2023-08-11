from collections import deque

def solution(board):
    
    moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    w, h = len(board[0]), len(board)
    visited = [[0] * w for _ in range(h)]
    
    def bfs(i, j):
        queue = deque()
        queue.append([i, j])
        
        while queue:
            x, y = queue.popleft()
            
            if board[x][y] == 'G':
                return visited[x][y]-1
                
            for move in moves:
                nx, ny = x, y
                while True:
                    nx += move[0]
                    ny += move[1]
                    if nx <0 or nx >= h or ny < 0 or ny >= w or board[nx][ny] == 'D':
                        nx -= move[0]
                        ny -= move[1]
                        break
                        
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]+1
                    queue.append([nx, ny])
                    
        return -1
                        
    
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'R':
                visited[i][j] = 1
                return bfs(i, j)