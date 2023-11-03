n=int(input())
mat1=[]
mat2=[]
t=0
for i in range(n):
    num=list(map(int,input().split())) [:n:]
    mat1.append(num)
for i in range(n):
    num=list(map(int,input().split())) [:n:]
    mat2.append(num)
r=[]
for i in range(n):
    diff=[]
    for j in range(n):
        t=abs(mat1[i][j]-mat2[i][j])
        diff.append(t)
    r.append(diff)
for num in r:
    print(" ".join(map(str,num)))
