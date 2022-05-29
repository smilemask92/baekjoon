import sys
input = sys.stdin.readline

N = int(input())
lst = [0] + list(map(int,input().split()))
dp = [0]*(N+1)
for ii in range(1,N+1):
    for jj in range(ii):
        if lst[jj]<lst[ii]:
            dp[ii] = max( dp[ii], dp[jj] + lst[ii])
print(*dp)
print(max(dp))
