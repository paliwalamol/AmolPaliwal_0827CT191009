marks1 = int(input("Marks of student : "))
if(marks1 > 90 and marks1 <= 100):
    print("Excellent")
elif(marks1 > 80 and marks1 <=90):
    print("A")
elif(marks1 > 70 and marks1 <= 80):
    print("B")
elif(marks1 > 60 and marks1 <= 50):
    print("C")
elif(marks1 > 50 and marks1 <= 60):
    print("D")
else:
    print("fail")