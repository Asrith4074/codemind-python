n=int(input())
num=list(map(int,input().split()))
m=int(input())
c=0
for i in num:
    if(i==m):
        c+=1
print(c)