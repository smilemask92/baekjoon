import sys
input = sys.stdin.readline
from collections import deque

def bfs(ii):
    Q = deque()
    Q.append(graph[ii])
    while Q:
        lst = Q.popleft()
        for node in lst:
            if visited[node] == 0:
                global cnt
                cnt += 1
                visited[node] = 1
                Q.append(graph[node])

N1 = int(input())
N2 = int(input())
graph = [[] for _ in range(N1+1)] # let first node empty
visited = [0]*(N1+1)

for _ in range(N2):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
visited[1] = 1
bfs(1)
print(cnt)