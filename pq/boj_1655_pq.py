import sys
import heapq
input = sys.stdin.readline

N = int(input())
h = []
for ii in range(N):
    elem = int(input())
    heapq.heappush(h,elem)
    ind = int((ii+1)/2+0.5)-1
    print(h)
    # print(f"size={len(h)} ind={ind} value={h[ind]} minvalue={h[0]} maxvalue={h[ii]}")
