'''4. Replace all the line containing SACRAMENTO to mumbai
and write output to another file.'''

import sys,csv

with open("realestate.csv", "r") as csvfile:
    readcolumn = csv.reader(csvfile)
    for column in readcolumn:
        city=column[1]
        print(city)
        if city == "SACRAMENTO":
            city.replace("SACRAMENTO","Mumbai")
    
        




'''cities=list(city)
realestate1.csv =[i for i in realestate.csv].replace("RIO LINDA", "Mumbai")'''


 
               
