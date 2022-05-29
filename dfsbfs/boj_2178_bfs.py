from collections import deque
import sys
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y0,x0):
    Q = deque()
    Q.append((y0,x0,1))
    while Q:
        y0,x0,val = Q.popleft()
        for dd in range(4):
            y1 = y0 + dy[dd]
            x1 = x0 + dx[dd]
            if x1<0 or y1<0 or x1>=M or y1>=N:
                continue
            if graph[y1][x1] != '1':
                continue
            graph[y1][x1] = val + 1
            Q.append((y1,x1,val+1))

N, M = map(int,input().split())
graph = [list(input().strip()) for _ in range(N)]
bfs(0,0)
print(graph[-1][-1])
