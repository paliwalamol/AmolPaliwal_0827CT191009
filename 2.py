# Write a program to fill in a letter template given below with name
# and date:
# letter = ‘’’ Dear <|Name|>
#  You are selected
#  <|Date|>’’’
import datetime
name=input()
curdate = datetime.date.today()

print(f'''Dear {name}
 You are selected
 {curdate}''')#here I used concept of f string