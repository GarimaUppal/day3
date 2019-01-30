name1 = "im Love Python prgramming"
name2 = "second string"
print ("original string:", name1)
#first character
print("First letter capital :" ,name1.capitalize())
#complete string in lower
print ("Complete string in lower:" ,name1.lower())
#complete string
print("Complete string in Upper:" , name1.upper())

#counts first letter
print(name1.count(name1))
#checking if name2 comes in name1
print(name1.count(name2))
print("Count of small p:" ,name1.count("p"))
print(name1.count("python"))
print("Total length of string with spaces :",len(name1))

#Checkinf total length of string without space count
print("Total number of words in string :", len(name1.split(" ")))

#split fucntion
print(name1.split(" "))
print(name2.split(" "))

#check if lower  -- to be checked
print(name1.islower())

#removes space at both the ends
name = "    python  hg"
print(name.strip())

#replace space at left side
print(name.lstrip())

#replaces python with perl
print(name1.replace("python","perl"))
name3 = "I love python because python is snake"
print(name3.replace("python","perl"))
newstring=name3.replace("python","perl")
print(newstring)
print (name3)



