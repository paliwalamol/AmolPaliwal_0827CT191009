s = input("enter string:")
n = int(input("enter n:"))
s = s[0:n].lower() + s[n:]
print(s)