a=int(input("enter number: "))
l=int(input("enter limit: "))
ans=0 
for i in range(0,l):
    p=1
    for j in range(0,i+1):
        p=p*a
    ans+=p
print(ans)

#Copyright @Amol Paliwal