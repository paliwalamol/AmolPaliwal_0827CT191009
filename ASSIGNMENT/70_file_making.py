import os
  

path = 'F:/simarjeet sir python assignment/ASSIGNMENT(70)'
  

for i in range(1,71):
 file = str(i) + '.py'
 with open(os.path.join(path, file), 'w') as fp:
    pass
  