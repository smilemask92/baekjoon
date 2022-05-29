import sys
input = sys.stdin.readline

def binarySearch(val,start,end):
    if end<start:
        return False
    divpoint = (start+end)//2
    if val==lst[divpoint]:
        return True
    elif val<lst[divpoint]:
        return binarySearch(val,start,divpoint-1)
    else:
        return binarySearch(val,divpoint+1,end)

N1 = int(input())
cards= list(map(int,input().split()))
cards.sort()
N2 = int(input())
lst = list(map(int,input().split()))

for item in lst:
    if binarySearch(item,0,N1-1):
        print(1,end=" ")
    else:
        print(0,end=" ")