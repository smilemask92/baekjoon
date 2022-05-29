import sys
input=sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
dp = lst.copy()

for ii in range(1,N):
    dp[ii] = max(lst[ii],dp[ii-1]+lst[ii])
    #다 버리고 현재부터 시작하거나. 아님 직전까지 가져온거를 앉고가던가.

print(*lst)
print(*dp)
print(max(dp))