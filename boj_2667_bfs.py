from collections import deque
import sys
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y0,x0):
    graph[y0][x0] = 2
    Q = deque()
    Q.append((y0,x0))
    while Q:
        y0,x0 = Q.popleft()
        for dd in range(4):
            y1 = y0 + dy[dd]
            x1 = x0 + dx[dd]
            if y1<0 or y1>=N or x1<0 or x1>=N:
                continue
            if graph[y1][x1] in [0,2]:
                continue
            global cnt
            cnt += 1
            graph[y1][x1] = 2
            bfs(y1,x1)

N = int(input())
graph = [list(map(int,list(input().rstrip()))) for _ in range(N)]


cntlst = []
for ii in range(N):
    for jj in range(N):
        if graph[ii][jj] in [0,2]:
            continue
        cnt = 1
        bfs(ii,jj)
        cntlst.append(cnt)

cntlst = sorted(cntlst)
print(len(cntlst))
print(*cntlst,sep="\n")
