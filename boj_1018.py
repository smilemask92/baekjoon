import sys
input = sys.stdin.readline

Nr,Nc=map(int,input().split())
li=[] #start with white 
for _ in range(Nr):
    temp=input()
    li.append(list(temp))

cnt=[0]*Nr*Nc

#상단좌측이 검정으로 시작해야만 하는 경우
ind=0
for ii in range(Nr):
    for jj in range(Nc):
        clr=li[ii][jj]
        if ii%2==0: # 홀수행
            if jj%2==0 and clr=='W': #홀수행&홀수열
                cnt[ii*Nc+jj]=1
            elif jj%2==1 and clr=='B': #홀수행&짝수열
                cnt[ii*Nc+jj]=1
        elif ii%2==1: # 짝수행
            if jj%2==1 and clr=='W': #짝수행&짝수열
                cnt[ii*Nc+jj]=1
            elif jj%2==0 and clr=='B': #짝수행&홀수열 
                cnt[ii*Nc+jj]=1

cntcase1=[]
cntcase2=[]
for j0 in range(Nc-7):
    for i00 in range(Nr-7):
        sumcrop1=0
        sumcrop2=0
        i0=i00
        for _ in range(8):
            rowsum=sum(cnt[i0*Nc+j0:i0*Nc+j0+8])
            # print("where row start %d rowsum: %d"%(i0,rowsum))
            sumcrop1+=rowsum
            sumcrop2+=(8-rowsum)
            i0+=1
        # print("sumcrop",sumcrop)        
        cntcase1.append(sumcrop1)
        cntcase2.append(sumcrop2)  

# print(cntcase1)
# print(cntcase2)
min1=min(cntcase1)
min2=min(cntcase2)
print(min(min1,min2))