import sys
input = sys.stdin.readline

def dfs(ii):
    visited[ii] = 1
    for node in graph[ii]:
        if visited[node] == 0:
            global cnt
            cnt += 1
            dfs(node)

N1 = int(input())
N2 = int(input())
graph = [[] for _ in range(N1+1)] # let first node empty
visited = [0]*(N1+1)

for _ in range(N2):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
dfs(1)
print(cnt)