import sys
input = sys.stdin.readline

def backtrack():
    if len(temp) == M:
        print(*temp)
        return
    else:
        for ii in range(1,N+1):
            if visited[ii] == 0: 
                temp.append(ii)
                visited[ii] = 1
                backtrack()
                temp.pop()
                visited[ii] = 0
        return

N,M = map(int,input().split())
temp = []
visited = [0]*(N+1)
backtrack()