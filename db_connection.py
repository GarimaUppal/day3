import pymysql

#open DB connection
db= pymysql.connect(host="localhost", port=3306 , user="root", passwd="Password@1", db="schlumberger")


#prepare a cursor object using () method
cursor = db.cursor()

#drop table
#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#create table
#sql = "create TABLE employee (firstname char(20) not null,lastname char(2),age int,sex char(1),income float)"

sql = "create TABLE realestate (street varchar(20) ,city char(2),zip int,state char(15),beds int,baths int, sq__ft float,type char(10),sale_date datetime,price float,latitude decimal,longitude decimal)"


cursor.execute(sql)
print("table created successfully")


#inserting
#sql="insert into employee (firstname,lastname,age,sex,income) values ('{}','{}',{},'{}',{})".\
#format('Girl','S',16,'F',70000)

#cursor.execute(sql)
#to commit DDL statements
db.commit()

#disconnect
db.close()
