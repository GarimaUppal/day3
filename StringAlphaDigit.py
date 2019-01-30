Stringinput= input("Enter the string: ")
value=list(Stringinput)
print(Stringinput)
print(value)
digit=0
alpha=0
for i in value:
    
    if i.isdigit():
        digit+=1
        print("Stringinput is digit",i)
        
    if i.isalpha():
        alpha+=1
        print("String is alphabet",i)
print (alpha, digit)

'''        
if Stringinput[i].isalpha():
        print("is Alphabet", i)
        #i+=1'''



