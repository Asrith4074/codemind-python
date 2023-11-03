r,c=map(int,input().split())
mat=[]
s=0
t=0
for i in range(r):
    inner=list(map(int,input().split()))
    mat.append(inner)
for j in mat:
    for x in j:
        if(x%2==0):
            s=s+x
        elif(x%2!=0):
            t=t+x
print(s,t)
        