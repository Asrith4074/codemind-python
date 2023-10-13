n=int(input())
num=list(map(int,input().split()))
s=0
m=0
for i in range(len(num)):
    if(i%2==0):
        s=s+num[i]
    elif(i%2!=0):
        m=m+num[i]
a=abs(m-s)
print(a)