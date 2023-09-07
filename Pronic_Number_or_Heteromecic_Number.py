n=int(input())
for i in range(1,n+1):
    #c=i*(i+1)
    if(i*(i+1)==n):
        break
if(i*(i+1)==n):
    print("YES")
else:
    print("NO")