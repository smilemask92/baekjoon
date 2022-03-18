import sys
input = sys.stdin.readline

N,K=map(int,input().split())
coins=[int(input()) for _ in range(N)]

temp=coins[:]
temp.append(K)
temp.sort()
where=temp.index(K)
coins=list(reversed(coins[:where+1]))
rem=K
cnt=0
i=0
while True:
    A=coins[i]
    mok=rem//coins[i]
    rem=rem%coins[i]
    # print("[%d]X%d and %d remain"%(coins[i],mok,rem))
    cnt+=mok
    if rem==0:
        break
    else:
        i+=1
print(cnt)