# 2×n 타일링 2
N = int(input())
dp = [0]*(N+1)
dp[1] = 1
dp[2] = 3
for ii in range(3,N+1):
    dp[ii] = dp[ii-1]+dp[ii-2]+dp[ii-2] # ii-2에다가 가로막대 2개를 붙이거나 또는 사각막대를 붙이거나. ii-1에다가 세로막대를 붙인다.
print(dp[N]%10007) 