import sys
input = sys.stdin.readline

testcases = int(input())

for _ in range(testcases):
    x1,y1,r1,x2,y2,r2 = list(map(int,input().split()))
    if [x1,y1,r1] == [x2,y2,r2]:
        print(-1)

    else:
        d = ((x2-x1)**2 + (y2-y1)**2)**0.5

        if d > (r1+r2):
            print(0) # two circles are not touched
        elif (d < abs(r2-r1)) and (r2 != r1):
            print(0)
        elif d == (r1+r2):
            print(1) # two circles are outer tangent
        elif d == abs(r2-r1):
            print(1) # two circles are inner tangent
        elif d < (r1+r2):
            print(2)