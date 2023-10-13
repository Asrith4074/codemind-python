n=int(input())
num=list(map(int,input().split()))
s=0
for i in num:
    s=s+i
avg=s//len(num)
print(avg in num)