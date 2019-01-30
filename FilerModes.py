#defualt file will be open in read mode
#fobj always checks for EOF

fobj = open("fileexists.txt", "r")

#Reads full file
for line in fobj:
    line=line.strip() #to remove blank lines in between
    print(line)


#display the output one at a time inllist format; is generally slow
print(fobj.readlines())



fobj.close()
