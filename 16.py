marks1 = int(input("Marks of student in subject 1: "))

marks2 = int(input("Marks of student in subject 2: "))

marks3 = int(input("Marks of student in subject 3: "))
#total assuming out of 50

if((marks1 / 50) * 100 < 33):
    print("fail")

elif((marks2 / 50) * 100 < 33):
    
    print("fail")

elif((marks3 / 50) * 100 < 33):

    print("fail")

elif((marks1 + marks2 + marks3) / 150 * 100 < 40):

    print("fail")

else:

   print("pass")