num = int(input("Enter the number for multiplication table : "))

#using for loop

print("Using for loop")

for i in range(1,11):
    print(num,'x ',i,' = ',num * i) 

i = 1

#using while loop

print("Using while loop")

while( i <= 10):
    print(num,'x ',i,' = ',num*i)
    i+=1