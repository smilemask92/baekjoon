import sys
input = sys.stdin.readline

W,H,X,Y,P = map(int,input().split())
R = H//2
cx1,cy1 = X,Y+R
cx2,cy2 = X+W,Y+R
cnt = 0
for _ in range(P):
    xpos,ypos = map(int,input().split())
    if X<=xpos<=X+W and Y<=ypos<=Y+H:
        cnt+=1
    elif ((xpos-cx1)**2 + (ypos-cy1)**2)**0.5 <= R:
        cnt+=1
    elif ((xpos-cx2)**2 + (ypos-cy2)**2)**0.5 <= R:
        cnt+=1
    

print(cnt)