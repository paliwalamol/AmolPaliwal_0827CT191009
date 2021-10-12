num = int(input("Enter a number: ")) 

sum = 0
number  = num
while(num > 0):
    sum += num
    num -= 1

print("The sum of",number , "natural numbers is: ", sum)