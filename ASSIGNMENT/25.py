def fact(n):
    if(n<=1):return 1;
    return n * fact(n-1)
n = int(input("enter a number:"))
print(fact(n))
#Copyright @Amol Paliwal