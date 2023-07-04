from collections import deque


def dfs(graph, node, visited):
    visited[node] = True
    print(node, end=" ")
    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, node, visited):
    queue = deque([node])
    visited[node] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
for i in range(1, n+1):
    graph[i].sort()
    

visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

dfs(graph, start, visited1)
print()
bfs(graph, start, visited2)
