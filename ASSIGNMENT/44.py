s = input("enter string:")
y=""
for i in range(len(s)):
    if(s[i]==" "):y=y+" "
y = y + s.replace(" ","")
# y=y + s
print(y)
#Copyright @Amol Paliwal