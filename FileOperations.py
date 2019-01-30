'''
1. Read and display the content of csv file
2. Display unique city names
3. Read display and count the lines where people are residing in RIO LINDA
output:
    display all the lines first
    no. of poeple residing in RIO LINDA : xxx

4. Replace all the line containing SACRAMENTO to mumbai and write output to another file.
5. Display only first 10 lines
6. reverse all the fields and display  like longi, lati, prive,sales_date ...
'''


#line starting with "WITH" you need not to close the file
#####################Context Manager##############3
''' 1.
with open("realestate.csv", "r") as fobj:
for line in fobj:
    print(line)
'''

######## second program ###############3

'''2 display unique city names'''
'''import sys,csv

unique_cities=set()

with open("realestate.csv", "r") as csvfile:
    readcolumn = csv.reader(csvfile)
    for column in readcolumn:
        city=column[1]
        #print (row[1])
        unique_cities.add(city)

for city in unique_cities:
    print(city)

 '''

########## Thrid program ############

import sys,csv

unique_cities=set()
count=0
csvfile = open("realestate.csv", "r")
#with open("realestate.csv", "r") as csvfile:
readcolumn = csv.reader(csvfile)

#row_count = len(readcolumn)
#print("total number of people ",row_count)

for column in readcolumn:
    city=column[1]
    if city == "RIO LINDA":
        count = count +1

#unique_cities.add(city)
#Linda_count=len(unique_cities)
#print("total number of cities where people are living", Linda_count)
print("total people living in RIO LINDA" , count)

csvfile.close()
        




