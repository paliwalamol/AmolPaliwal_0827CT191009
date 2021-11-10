s=input("enter string:")
d = {}
for i in range(0,len(s)):
    if s[i] in d.keys():
        d[s[i]]=1 + d[s[i]]
    else:
       d[s[i]] = 1 
print(d)