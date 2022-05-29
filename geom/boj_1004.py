import sys
input = sys.stdin.readline

def isincircle(a,b,cx,cy,r):
    d = ((cx-a)**2 + (cy-b)**2)**0.5
    return True if d<r else False

T = int(input())
for testcase in range(1,T+1):
    x1,y1,x2,y2 = map(int,input().split())
    N = int(input())
    cnt = 0
    for _ in range(N):
        cx,cy,r = map(int,input().split())
        checker = [0,0]
        if isincircle(x1,y1,cx,cy,r):
            checker[0]=1
        if isincircle(x2,y2,cx,cy,r):
            checker[1]=1
        if sum(checker)==1:
            cnt+=1


    print(f"testcase {testcase}: {cnt}")
