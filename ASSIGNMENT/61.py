import math
def calculate_distance(a):
    if(str(type(a))=="<class 'float'>" or str(type(a))=="<class 'int'>"):
        return abs(a)
    else:
        return "No value"

print(calculate_distance(9))
print(calculate_distance(9.6))
print(calculate_distance("what?"))
#Copyright @Amol Paliwal