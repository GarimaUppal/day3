import os
for files in os.listdir("C:\\TEMP"):
     print("filenames",files)
     if files.endswith('.txt'):
         print("filename", files)
     

     
'''files = list_files(directory, "py")
for f in files:
    print("filenames",f)

files = filter(os.path.isfile, os.listdir('.')) 
dirs = filter(os.path.isdir, os.listdir('.'))

for file in os.listdir("C:\\TEMP"):
    if file.endswith(".txt"):
        print(os.path.join("/mydir", file))

#list files in particular directory
        for filename in os.listdir("C:\\TEMP"):
    print("filename", filename)'''

#last successful command run
status = os.system("bash hello.sh")
if status == 0:
    print("success")

#listing files are dircteories separately
files=[]
dir=[]
for file in os.listdir():
    if os.path.isfile(file):
        files.append(file)
        of os.path.isdir(file):
            dirs.append(file)

            print("files")
            print("------")
            for file in files:
                print(file)

                print ("dirs")
                print("-----")
                for file in dirs:
                    print(file)


