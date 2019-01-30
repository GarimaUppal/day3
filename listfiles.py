import os
print(os.getcwd())
files=[]
dirs=[]
for file in os.listdir():
    if os.path.isfile(file):
        files.append(file)
    if os.path.isdir(file):
        dirs.append(file)

print("files")
print("------")
for file in files:
    print(file)
print ("dirs")
print("-----")
for file in dirs:
    print(file)
