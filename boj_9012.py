import sys
input = sys.stdin.readline

N=int(input())
for _ in range(N):
    li=[]
    ans='idk' # at this point, we don't know
    line=sys.stdin.readline().rstrip()
    for chr in line:
        if chr=='(':
            li.append(1)
        else: # chr==')':
            if len(li)==0:
                ans='NO'
                break
            else:
                li.pop()
    if ans=='idk' and len(li)==0:
        ans='YES'
    elif ans=='idk' and len(li)>0:
        # print(li)
        ans='NO'
    print(ans)