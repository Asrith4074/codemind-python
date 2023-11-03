r,c=map(int,input().split())
mat=[]
s=0
for i in range(r):
    inner_list= list(map(int,input().split()))
    mat.append(inner_list)
for x in range(c):
    for y in range(r):
         s += mat[y][x]
    print(s , end=" ")
    s=0