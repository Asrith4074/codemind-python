n=int(input())
num=list(map(int,input().split()))
a,b=map(int,input().split())
m=0
for j in range(len(num)):
    if(num[j]<a or num[j]>b):
        s+=num[j]
print(s)