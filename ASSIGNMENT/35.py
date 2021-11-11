def interchange(a,b):
    x = a[ 0 : 2 ]
    a = a.replace(a[ 0 : 2 ],b[ 0 : 2 ])
    b = b.replace(b[ 0 : 2 ],x)
    print(a + " " +b)

a,b = map(str,input().split(" "))
interchange(a,b)
#Copyright @Amol Paliwal