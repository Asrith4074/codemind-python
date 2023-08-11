import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))
d=math.sqrt(area)
print(f"{d:.2f}")