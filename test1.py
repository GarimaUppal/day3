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
