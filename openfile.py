fobj = open("customers.txt","w")
fobj.write("python\n")
fobj.write("perl\n")
#doesnot accept intso either typecast or use "
#fobj.write(100)

fobj.write(str(100))
fobj.write("  200")
fobj.close()
