
s=input("enter string:")
if(len(s)<3):print(s)
elif(s.endswith("polis")):
    # s.replace("polis","polisCS")
    print(s + "CS")
else:
    # s.replace(s[len(s)-1],s[len(s)-1]+"polis")
    print(s + "polis")