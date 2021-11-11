def area(l,b):return l*b
def call(l,b):
    return area(l,b) + area(l+1,b-1) + area(l,b+1)
print(call(2,2))
#Copyright @Amol Paliwal