import sys
input = sys.stdin.readline

def backtrack(startnum):
    if len(temp)==M:
        print(*temp)
        return
    else:
        for ii in range(startnum,N+1):
            if visited[ii]==0:
                temp.append(ii)
                visited[ii]=1
                backtrack(ii+1)
                temp.pop()
                visited[ii]=0
        return


N,M = map(int,input().split())
temp = []
visited = [0]*(N+1)
backtrack(1)
