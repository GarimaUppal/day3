


import sys,csv

unique_cities=set()
count = 0
csvfile = open("realestate.csv", "r")
#with open("realestate.csv", "r") as csvfile:
readcolumn = csv.reader(csvfile)

for column in readcolumn:
    #print(line)
    city=column[1]
    if city  == "RIO LINDA":
        count = count + 1
    
    
#Linda_count=len(unique_cities)

print("total people living in RIO LINDA" , count)


csvfile.close()
        
