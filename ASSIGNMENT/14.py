print ("Enter first age")
first = input()
print ("Enter second age")
second = input()
print ("third age")
third = input()

if first >= second and first >= third:
  print ("Oldest is",first)
elif second >= first and second >= third:
  print ("Oldest is",second)
elif third >= first and third >= second:
  print ("Oldest is",third)
else:
  print ("All are equal")