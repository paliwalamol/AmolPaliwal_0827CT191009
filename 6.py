# Write a program to enter marks of 6 students and display them in
# sorted order.
marks = []
print("enter marks of 6 students")
for i in range(7):
    marks.append(int(input()))
marks.sort()
print(marks)