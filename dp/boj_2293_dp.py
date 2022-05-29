import sys
input = sys.stdin.readline

N, K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
coins.sort()
dp = [0]*(K+1)
for coin in coins:
    for i in range(coin,K+1):
        if i%coin == 0:
            dp[i] += 1
        elif dp[i-coin]!=0:
            dp[i] += 1
    print(*dp)
print(*dp)
