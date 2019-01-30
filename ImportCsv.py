import csv
import MySQLdb

db= pymysql.connect(host="localhost", port=3306 , user="root", passwd="Password@1", db="schlumberger")
cursor = db.cursor()


csv_data = csv.reader(file('realestate.csv'))
for row in csv_data:

    sql= ('INSERT INTO realestate(street,city,zip,state,beds,baths,sq__ft,type,sale_date,price,latitude,longitude)\
    VALUES("{}","{}",{},"{}",{},{},{},"{}",{},{},{},{})' format (csv_data))

cursor.execute(sql)
 
#close the connection to the database.
db.commit()
db.close()
