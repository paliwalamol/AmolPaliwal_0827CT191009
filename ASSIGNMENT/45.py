s = input("enter string:")
d={}
for i in range(len(s)):
    if s[i] in d.keys():
        d[s[i]]= 1 + d[s[i]]
    else:
       d[s[i]] = 1 
max = 0
# print(d)
for key in d.keys():
    if d[key]>max:max=d[key]
# print(max)
for key in d.keys():
    if d[key]==max:
       print(key)
