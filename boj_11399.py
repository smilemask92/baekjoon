import sys
input = sys.stdin.readline

N=int(input())
P=list(map(int,input().split()))
P.sort()
time=[sum(P[0:i+1]) for i in range(N)]
print(sum(time))