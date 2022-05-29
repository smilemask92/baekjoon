import sys
input=sys.stdin.readline

N = int(input())
lst = [int(input()) for  _ in range(N)]
dp = [0]*N
dp[0] = lst[0]
dp[1] = dp[0] + lst[1]

for ii in range(N):
    case1 = lst[ii]+lst[ii-1]+dp[ii-3] # a,c,d
    case2 = lst[ii]+dp[ii-2] #a,b,d
    case3 = dp[ii-1] # a,b,c
    dp[ii] = max([case1,case2,case3])

print(dp[N-1])