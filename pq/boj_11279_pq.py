import sys
import heapq
input = sys.stdin.readline


N = int(input())
h = []
for _ in range(N):
    elem = int(input())*-1
    if elem==0:
        if len(h)==0:
            print(0)
        else:
            print(-1*heapq.heappop(h))
    else:
        heapq.heappush(h,elem)