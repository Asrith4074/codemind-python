x,y=map(int,input().split())
for i in range(max(x,y), 1 + (x * y)):
    if i % x == i % y == 0:
        lcm = i
        break
print(lcm)