l = input("enter string:")
a = l[1]
b = l[len(l)-1]

m = l.replace(l[len(l)-1],a)
m = m.replace(l[1],b)
print(m)
# doubt
#Copyright @Amol Paliwal