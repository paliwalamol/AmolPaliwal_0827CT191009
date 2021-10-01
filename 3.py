# Write a program to detect double spaces in a string.

string = "hello  my   name   is  Amol  Paliwal"
l = string.find("  ")

if l==-1:
    print("no double spaces")
else:
    print("double space present")




