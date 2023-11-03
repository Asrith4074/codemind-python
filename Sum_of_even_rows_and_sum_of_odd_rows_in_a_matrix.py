r,c=map(int,input().split())
s=0
t=0
mat=[]
for i in range(r):
    inner=list(map(int,input().split()))
    mat.append(inner)
for x in range(r):
    for y in range(c):
        if(x%2==0):
            s=s+mat[x][y]
        elif(x%2!=0):
            t=t+mat[x][y]
print(s,t)