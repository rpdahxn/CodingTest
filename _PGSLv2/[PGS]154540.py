import sys
sys.setrecursionlimit(1000000)

def solution(maps):
    answer = []
    idx = -1

    h, w = len(maps), len(maps[0])
    
    visited = [[False] * w for _ in range(h)]
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    
    def dfs(i, j):
        visited[i][j] = True
        
        for move in moves:
            ni = i + move[0]
            nj = j + move[1]
            if 0 <= ni < h and 0 <= nj < w and maps[ni][nj] != 'X' and not visited[ni][nj]:
                answer[idx] += int(maps[ni][nj])
                dfs(ni, nj)
        
        return
        
    for i in range(h):
        for j in range(w):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(int(maps[i][j]))
                idx += 1
                dfs(i, j)
    
    if not answer:
        answer = [-1]
    else:
        answer.sort()
    
    return answer