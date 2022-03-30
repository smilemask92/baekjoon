import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(ii,key):
    for node in graph[ii]:
        if visited[node] == 1:        
            if di[node] == key:
                return False
        elif visited[node] == 0:
            otherkey = 'b' if key == 'a' else 'a'
            di[node] = otherkey
            visited[node] = 1
            isBipartite = dfs(node,otherkey)
            if isBipartite == False:
                return False


T = int(input())
for _ in range(T):
    nodecnt,linecnt = map(int,input().split())
    graph = [[] for _ in range(nodecnt+1)]  
    for ii in range(linecnt):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [0]*(nodecnt+1)
    di = dict()
    answer = "YES"
    for ii in range(1,nodecnt+1):
        if visited[ii] == 0:
            visited[ii] = 1
            di[ii] = 'a'
            isBipartite = dfs(ii,'a')
        if isBipartite == False:
            answer = "NO"
            break
    print(answer)