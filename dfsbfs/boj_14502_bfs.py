from itertools import combinations
import copy
from collections import deque
import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

dy = [0,0,-1,1]
dx = [-1,1,0,0]

N,M = map(int,input().split())
board0 = [list(map(int,input().split())) for _ in range(N)]


wall = []
safe = []
safecnt0 = 0
Q0 = deque()
for ii in range(N):
    for jj in range(M):
        if board0[ii][jj] == 1:
            wall.append([ii,jj])
        elif board0[ii][jj] == 2:
            Q0.append([ii,jj])
        else:
            safe.append([ii,jj])
            safecnt0 += 1


possiblesafecnt = []
for cases in combinations(safe,3): #빈자리에서 3개 뽑기.
    board = copy.deepcopy(board0)
    safecnt = safecnt0
    Q = copy.deepcopy(Q0)
    for yy,xx in cases:
        board[yy][xx] = 1
    while Q:
        y0,x0 = Q.popleft()
        for dd in range(4):
            y1 = y0 + dy[dd]
            x1 = x0 + dx[dd]
            if x1<0 or y1<0 or x1>=M or y1>=N:
                continue
            if board[y1][x1] != 0:
                continue
            board[y1][x1] = 2
            safecnt -= 1
            Q.append((y1,x1))

    possiblesafecnt.append(safecnt)




# print(possiblesafecnt)
print(max(possiblesafecnt)-3)