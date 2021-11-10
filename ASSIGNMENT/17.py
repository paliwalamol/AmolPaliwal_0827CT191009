def taxes(income):
    while True:
        if income < 10000:
            tax = 0
        elif income > 10000 and income <= 20000:
            tax = (income-10000)*(0.1)
        elif income > 20000 :
            tax = (income-20000)*(0.2) + 2000
    
    return tax
a=int(input("enter income:"))
print("tax:" + taxes(a))