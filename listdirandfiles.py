import os
print(os.getcwd())
for file in os.listdir("C:/Users/GUppal/Desktop/pythonprograms"):
    if file.endswith(".txt"):
        print(os.path.join("text files are :", file))
    if file.endswith(".py"):
        print(os.path.join(os.getcwd(),file))

os.chdir("C://Users/GUppal/Desktop/flexera")
print(os.getcwd())
subdirs = [x[0] for x in os.walk('.')]
print(subdirs)



                    
