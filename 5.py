# Write a program to store seven fruits in a list entered by the user

fruits=[]
print("enter names of seven fruits")
for i in range(7):
    fruit = input()
    fruits.append(fruit)
print(fruits)