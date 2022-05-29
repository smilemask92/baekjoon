N = int(input())
dp = list(range(100001))
root = int(N**0.5)
lst = list(range(1,root+1))
for numb in lst:
    square = numb**2
    for ii in range(1,N+1):
        if ii%square==0:
            dp[ii] = min(dp[ii],ii//square)
        else:
            mod = ii%square
            dp[ii] = min(dp[ii],dp[ii-mod]+dp[mod])
print(dp[N])