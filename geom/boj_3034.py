import sys
input = sys.stdin.readline

N,W,H = map(int,input().split())
lst = [int(input()) for _ in range(N)]
hyp = (W**2 + H**2)**0.5
for item in lst:
    if item<=hyp:
        print("DA")
    else:
        print("NE")