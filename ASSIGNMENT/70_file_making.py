# for making 70 files
import os
path = 'F:/simarjeet sir python assignment/ASSIGNMENT'
for i in range(1,71):
 file = str(i) + '.py'
 with open(os.path.join(path, file), 'a') as fp:
    pass



# for appending lines
import os
path = 'F:/simarjeet sir python assignment/ASSIGNMENT'
for i in range(1,71):
 file = str(i) + '.py'
 with open(os.path.join(path, file), 'a') as fp:
    fp.write("\n#Copyright @Amol Paliwal")
    fp.close()



# Copyright @Amol Paliwal

