from collections import deque
import sys
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

M,N = map(int,input().split())
graph = [input().split() for _ in range(N)]

Q = deque()
ripecnt = 0
noripecnt = 0
wallcnt = 0
for ii in range(N):
    for jj in range(M):
        if graph[ii][jj] == '1':
            ripecnt += 1
            Q.append((ii,jj,0))
        elif graph[ii][jj] == '0':
            noripecnt += 1
        else:
            wallcnt += 1

if N*M - wallcnt - ripecnt == 0:
    print(0)
else:
    addripe = 0
    days = []
    while Q:
        y0,x0,val = Q.popleft()
        for dd in range(4):
            y1 = y0 + dy[dd]
            x1 = x0 + dx[dd]
            if x1<0 or y1<0 or x1>=M or y1>=N:
                continue
            if graph[y1][x1] != '0':
                continue
            graph[y1][x1] = val+1
            addripe += 1
            Q.append((y1,x1,val+1))
            days.append(val+1)
    if noripecnt == addripe:
        print(max(days))
    else:
        print(-1)