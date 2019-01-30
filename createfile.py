import pathlib
import datetime
import os
print(os.getcwd())
pathlib.Path("newfile.txt").touch()
pathlib.Path("newfile.csv").touch()
pathlib.Path("newfile.xls").touch()


#datestring = datetime.strftime(datetime.now(), '%Y/%m/%d_%H:%M:%S')
import time
timestr = time.strftime("%Y%m%d%H%M%S.log")
print(timestr)
pathlib.Path(timestr).touch()
timestr1 = time.strftime("%Y_%m_%d.log")
timestr2 = time.strftime("%Y_%b_%d.log")
print(timestr1)
pathlib.Path(timestr1).touch()
pathlib.Path(timestr2).touch()

