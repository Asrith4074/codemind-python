n=int(input())
num=list(map(int,input().split()))
s=0
for i in range(len(num)):
    if (num[i]%2!=0):
        s=i
print(s)
    