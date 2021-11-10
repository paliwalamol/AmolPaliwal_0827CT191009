s = input("enter string:")
s = s[0].upper() + s[1:len(s)-1] + (s[len(s)-1].upper() if len(s)>1 else "")
print(s)