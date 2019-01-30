'''Stringinput= input("Enter the string: ")
#print("number of words in string: ",len(Stringinput.split(" ")))
file=Stringinput.split(" ")
print("String split" , file)
alist=list(Stringinput)
alist.reverse()
#print(str(alist))
def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
print(reverse_string_words("Python Exercises."))'''


name=input("Enter the string: ")
print(name[::-1])


