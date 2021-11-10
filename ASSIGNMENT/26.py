def fact(n):
    if(n<=1):return 1;
    return n * fact(n-1)

d={}

for i in range(0,10):
    d[str(i)]=fact(i)

n = (input("enter a number:"))
sum=0
for i in range(len(n)):
    sum=sum+d[n[i]]
if(sum==int(n)):
    print("strong number")
else:
    print("not strong number")