n=int(input())
num=list(map(int,input().split()))
s=0
m=0
for i in num:
    if(i%2==0):
        s=s+i
    elif(i%2!=0):
        m=m+i
b=abs(s-m)
print(b)
    