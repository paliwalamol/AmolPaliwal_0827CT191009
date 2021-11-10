def calculateBill(units):
 
    if (units <= 100):
      
        return units * .5;
     
    elif (units <= 200):
     
        return ((100 * .5) +
                (units - 100) * .75);
     
    elif (units <= 300):
      
        return ((100 * .5) +
                (100 * .75) +
                (units - 200) * 1.2);
     
    elif (units > 300):
     
        return ((100 * .5) +
                (100 * .75) +
                (100 * 1.2) +
                (units - 300) * 1.5);
     
    return 0;
 

a=int(input("enter units:"))
bill = calculateBill(a)
bill = bill + bill *.2
print(bill);