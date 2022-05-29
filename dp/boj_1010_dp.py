import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    a,b= map(int,input().split())
    if a==b:
        print(1)
        continue
    if a>b:
        a,b = b,a
    dif = b - a
    dp=[[1]*dif for _ in range(a)]
    for ii in range(a):
        for jj in range(dif):
            if ii == 0:
                dp[ii][dif] = dif
            else:
                dp[ii][dif] = dp[ii-1][dif]


