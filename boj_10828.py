import sys
input = sys.stdin.readline

li=[]
N=int(sys.stdin.readline())
for _ in range(N):
    ask=sys.stdin.readline().rstrip().split()
    if ask[0]=='push':
        li.append(int(ask[-1]))
    elif ask[0]=='pop':
        if len(li)>=1:
            print(li[-1])
            li.pop()
        else:
            print(-1)
    elif ask[0]=='size':
        print(len(li))
    elif ask[0]=='empty':
        if len(li)==0:
            print(1)
        else:
            print(0)
    elif ask[0]=='top':
        if len(li)>=1:
            print(li[-1])
        else:
            print(-1)