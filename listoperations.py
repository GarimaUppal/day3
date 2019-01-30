alist=[10,20,30,40]
print(alist)
alist.append(50)
alist.append(60)
print("after appending:",alist)

alist.extend([80,90,100])
print("after extending multiple values at one time:", alist)

print("no. of occurance of 10:",alist.count(10))
print("index of 40: ", alist.index(40))

alist.insert(0,5)
print("after inserting :", alist)

removed=alist.pop(0)
print("removed value is :",removed)

alist.reverse()
print("after reversing", alist)

alist.clear()
print(alist)


