n=int(input())
m=int(input())
s=0
x=0
for i in range(1,n):
        if(n%i==0):
            s=s+i
for j in range(1,m):
         if(m%j==0):
             x=x+j
if(x==n and s==m):
    print("Amicable")
else:
    print("Not Amicable")