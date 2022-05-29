from collections import deque
import sys
input = sys.stdin.readline

def dfs(ii):
    # dfs version 2. Mark right before visit. You already did visit-mark.
    print(ii,end=" ")
    for node in graph[ii]:
        if visited[node] == 0:
            visited[node] = 1 # dfs version 2. Mark right before visit
            dfs(node)

def bfs(ii):
    print(ii,end=" ")
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


# dfs version 1. Mark right after visit
visited = [0]*(N+1)
visited[V] = 1
dfs(V)
print("")

# bfs
visited = [0]*(N+1)
visited[V] = 1
bfs(V)
print("")