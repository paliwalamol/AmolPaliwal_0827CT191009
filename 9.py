# Write a program to count the number of zeroes in following tuple.
# a = (7,0,8,0,0,9)

a = (7,0,8,0,0,9)
c=0
for i in a:
    if(i==0):
        c=c+1
print(c)