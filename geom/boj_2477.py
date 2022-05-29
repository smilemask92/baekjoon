import sys
input = sys.stdin.readline

K = int(input())
lst = []
for _ in range(3):
    d,l = map(int,input().split())
    lst.append(l)
    d,l = map(int,input().split())
    lst.append(l)

horiz = [lst[0],lst[2],lst[4]]
vert = [lst[1],lst[3],lst[5]]
maxWidth = max(horiz)
maxHeight = max(vert)
posmaxwidth = lst.index(maxWidth)
lst = lst[posmaxwidth:] + lst[:posmaxwidth]
if lst[1] != maxHeight: # in case of maxHeight is at 5th
    lst = [lst[5]] + lst[:5]
square = lst[0]*lst[1] - lst[3]*lst[4]
print(square*K)