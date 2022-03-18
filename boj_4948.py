import sys
input = sys.stdin.readline

A=int(input())
while A>0:
    B=A*2
    given=set(range(A+1,B+1))
    B2=int((B+1)**0.5)
    for i in range(2,B2):
        temp=set(range(i,B2,i))-{i}
        given=given-temp
    prime=list(given-{1})
    # print(sorted(prime),"and",len(prime))
    print(len(prime))
    A=int(input())