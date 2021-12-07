n = int(input())

graph = []

for _ in range(n):
    graph.append(list(input()))

# 연결된 집들으 다 돌기 -> dfs ?
# 스택 & 재귀함수
# return True면 ++ 하면서 연결된 집들 개수 세기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(graph, x, y):
    count = 0
    graph[x][y] = 0  # 방문 표시
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == '1':  # 아직 방문하지 않은 노드라면
                count += dfs(graph, nx, ny)
    return count


count_list = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            count_list.append(dfs(graph, i, j))
print(len(count_list))
count_list.sort()
for count in count_list:
    print(count)
