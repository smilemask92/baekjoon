import sys
input = sys.stdin.readline

A=[]
N=int(sys.stdin.readline())
for _ in range(N):
    ask=int(sys.stdin.readline())
    if ask==0:
        A.pop()
    else:
        A.append(ask)
print(sum(A))