import os
#os.mkdir("newfolder")
#path="D:\WHITEHAT JR CLASSWORKS\C-919"
#a = os.path.exists(path)
#print(a)
import shutil
source = input("enter source folder name")
destination = input("destination folder name")
source=source+'/'
destination = destination + '/'
listoffile=os.listdir(source)
for i in listoffile:
   # shutil.copy((source+i),destination)
   shutil.move((source+i),destination)