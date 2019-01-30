'''capture the string "Python is general purpose interpreted cross platform programming lan" from the keyboard and perform the below operations
1. display the string in uppercare
2. count  number of occurances of p in the string and display it
3. replace python to ruby in string
4. count number of words in string  ... len(str.split(" ")
5. count number of characters and display...len(str)
6. remove spaces if any ''' 

Stringinput= input("Enter the string: ")
print("Complete string in Upper:" , Stringinput.upper())
print("Count of small p:" ,Stringinput.count("p"))
print(Stringinput.replace("Python","ruby"))
print("number of words in string: ",len(Stringinput.split(" ")))
print("number of characters: ",len(Stringinput))
print(Stringinput.strip())
#print(Stringinput.replace(" ","")


#display all duplicates of the list
alist=[10,20,30,40,40,40,50]
print("Unique Values are")
print(list(set(alist)))

# capture filename from keyboard and display filename and extension separately

Nameoffile= input("Enter filename:" )
File=Nameoffile.split(".")

#File=list(Listfile)
#print(Filename)
print("Filename: ",File[0])
print("Extension: ",File[1])



#take input of two numbers and display their sum

number1= input("Enter number 1:" )
num1=int(number1)
number2= input("Enter number 2:" )
num2=int(number2)
sumoftwo=sum([num1,num2])
print("SUM :",sumoftwo)


'''define empty list in your program and perform all below operations:
1. append 10 to list
2. append 20
3.append 50
4.extend with 90,20,45,32,645,32,90,65,43,23,55,4,32,50
5. remove all duplicates
6. remove 50 from list
7. sort all elements in descending
8. convert list to tuple and display it'''

alist=[10,20,30,40,50,60]
print(alist)
alist.append(10)
print(alist)
alist.append(20)
print(alist)
alist.append(50)
print(alist)
alist.extend([90,20,45,32,645,32,90,65,43,23,55,4,32,50])
print(alist)
alist=set(alist)
print("After removing duplicates",alist)
alist=list(alist)
alist.remove(50)
print("After removing 50:",alist)
alist.sort(reverse=True)
print("in descending order: ", alist)
alist=tuple(alist)
print("Values in tuple", alist)





