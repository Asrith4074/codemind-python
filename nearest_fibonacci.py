n=int(input())
num1 = 0
num2 = 1
s= 0

while num2 < n:
    s=num1+num2
    num1, num2 = num2, s
if(num2==s):
    num2=num1
k=n-num2
l=s-n
# print(num1,num2,s,k,l)
if(k>l):
    print(s)
elif(l>k):
    print(num2)
else:
    print(num2,s)
    

