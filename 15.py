num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))
num4 = int(input("Enter 4th number : "))

if num1 > num4 :
    f1 = num1
else :
    f1 = num4

if num2 > num3 :
    f2 = num2
else : 
    f2 = num3

if f1 > f2 :
    print(f1, "is greatest")

else :
    print(f2, "is gratest")
    