import sys
input = sys.stdin.readline

def bt(startpos):
    if len(temp)==6:
        print(*temp)
    else:
        for ii in range(startpos,N):
            if visited[ii]==0:
                visited[ii]=1
                temp.append(lst[ii])
                bt(startpos+1)
                temp.pop()
                visited[ii]=0

while True:
    lst = list(map(int,input().split()))
    if lst[0] == 0:
        break
    N = lst[0]
    lst = lst[1:]
    temp = []
    visited = [0]*N
    bt(0)

    print("")
