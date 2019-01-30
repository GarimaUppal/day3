''' check if files exists ,
if it does , show error else create a file and
write even numbers from 500 to 300 and close'''

import time
import datetime
import pathlib
import os

#os.path.isfile(filename)

filename = time.strftime("Even_Numbers%Y%m%d.log")
#filename = Path("C:/Users/GUppal/Desktop/python")

if os.path.exists("C:/Users/GUppal/Desktop/python"):
    if not os.path.isfile(filename):
        # file exists    
        fobj = open(filename,"w")
        fobj.write("Even numbers from 500 to 300")
        for line in range(500,300,-2):
            fobj.write((str(line)+ "\n"))
        fobj.close()    
else:
    print("file doesn't exit")
    sys.exit(1)


#pathlib.Path(timestr).touch()
#for i in range(500,300,-2):
#   print(i, end=', ')
#fobj.write(str(range(500,300,2)))


#exists : whether it can be file or directory
#isfile :only for file
#isdir  : only for directory
