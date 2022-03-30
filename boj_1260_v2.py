from collections import deque
import sys
input = sys.stdin.readline

def dfs(ii):
    print(ii,end=" ")
    visited[ii] = 1
    for node in graph[ii]:
        if visited[node] == 0:
            # dfs version 1. Mark visit. So don't need to mark_visit any at this point
            dfs(node)

def bfs(ii):
    print(ii,end=" ")
    visited[ii] = 1
    Q = deque()
    Q.append(graph[ii])
    while Q:
        lst = Q.popleft()
        for node in lst:
            if visited[node] == 0:
                print(node,end=" ")
                visited[node] = 1
                Q.append(graph[node])



N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)] #let first node empty
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for ii in range(1,N+1):
    graph[ii] = sorted(graph[ii])


# dfs version 2. Mark right before visit
visited = [0]*(N+1)
dfs(V)
print("")

# bfs
visited = [0]*(N+1)
bfs(V)
print("")