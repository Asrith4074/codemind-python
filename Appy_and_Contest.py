t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    f=0
    l=0
    y=n//a
    f+=y
    x=n//b
    l+=x
    m=n//(a*b)
    s=f+l-m
    if(s>=k):
        print("Win")
    else:
        print("Lose")