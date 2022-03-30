import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(ii):
    for node in graph[ii]:
        if visited[node] == 1:
            continue
        else:
            visited[node] = 1
            dfs(node)
            pass

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)] #let first node 0 is empty
visited = [0]*(N+1)

for ii in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for ii in range(1,N+1):
    if visited[ii] == 0:
        cnt += 1
        dfs(ii)
print(cnt)