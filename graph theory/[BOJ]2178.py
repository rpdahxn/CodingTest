from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(input()))  # 띄어쓰기 없이 문자열로 받기

graph[0][0] = 1  # graph를 int형으로 선언
# print(graph)

# 최단 거리 -> bfs

# 이동할 네 방향 정의 (상, 하, 좌, 우)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if graph[nx][ny] == '1':
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]


print(bfs(0, 0))
