

a = int(input("enter number:"))
p=0
if a<24:
    if a%8==0 or a%12==0:
        p=1
else:
    if a%24==0:
        p=1


print(p>0 and "yes" or "no")