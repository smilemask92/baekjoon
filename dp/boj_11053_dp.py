import sys
input=sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
dp = [1]*N

for ii in range(1,N):
    for jj in range(ii):
        if lst[jj]<lst[ii]:
            case1 = dp[ii]
            case2 = dp[jj]+1
            dp[ii] = max(case1,case2)
print(max(dp))
