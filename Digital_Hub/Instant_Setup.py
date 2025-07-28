import mysql.connector

def instant_setup():
     host = input("You Host Name: ")
     user = input("Your User Name: ")
     password = input('Your Password: ')

     try:
               connection = mysql.connector.connect(
                    host = host,
                    user = user,
                    passwd = password
                    )
               cursor = connection.cursor()
               if connection.is_connected:
                    print("Connection Stablised Succesfully")

     except mysql.connector.Error as s:
               print("Error: {}".format(s))

     print("Initiating Instant Setup")
     database = "Digital_Hub"
     cursor.execute("show databases like '{}'".format(database))
     exists = cursor.fetchone()

     while True:
          if exists:
               cursor.execute("drop database {}".format(database))
               print("Creating Database \"Digital_Hub\" ")
               cursor.execute("create database Digital_Hub")
               print("Database \"Digital_Hub\" Created Succesfully")
               break

          else:
               print("Creating Database \"Digital_Hub\" ")
               cursor.execute("create database Digital_Hub")
               print("Database \"Digital_Hub\" Created Succesfully")
               break

     cursor.execute("use Digital_Hub")

     print("Initiating Data setup\n")
     print("Initiating Step 1\n")
     cursor.execute("create table Customers(Customer_Name varchar(50), Customer_Phone_Number int, Total_Bill int)")
     print("Customer Table Created Successfully")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     print("Initializing Step 2\n")
     print("Creating Employees Table\n")
     print("Inserting Values Into Employee Table\n")
     cursor.execute("create table Employees(Employee_Id int primary key, Employee_Name varchar(50), Designation varchar(50), Salary int)")
     print("Employee Table Created Succesfully\n")
     cursor.execute("insert into Employees values(171380,'Kairav Rajiv Jaiswal','Ceo',500000)") #1
     connection.commit()
     print("First value Inserted\n")
     cursor.execute("insert into Employees values(965413,'Neha Mittal','Senior Manager',50000)")#2
     connection.commit()
     print("Second value Inserted\n")
     cursor.execute("insert into Employees values(854121,'John Depp','Senior Manager',50000)")#3
     connection.commit()
     print("Third value Inserted\n")
     cursor.execute("insert into Employees values(695741,'Karan Rajput','Manager',50000)")#4
     connection.commit()
     print("Fourth value Inserted\n")
     cursor.execute("insert into Employees values(958471,'Derek','Manager',50000)")#5
     connection.commit()
     print("Fifth value Inserted\n")
     cursor.execute("insert into Employees values(965871,'Remika Sen','Assistant',50000)")#6
     connection.commit()
     print("Sixth value Inserted\n")
     cursor.execute("insert into Employees values(325698,'Prakriti Yadav','Assistant',50000)")#7
     connection.commit()
     print("Seventh value Inserted\n")
     cursor.execute("insert into Employees values(754123,'Aman Rhodes','Co-Worker',50000)")#8
     connection.commit()
     print("Eighth value Inserted\n")
     cursor.execute("insert into Employees values(584731,'Yasmin Ansari','Co-worker',50000)")#9
     connection.commit()
     print("Ninth value Inserted\n")
     cursor.execute("insert into Employees values(35241,'Junade Shergil','worker',50000)")#10
     connection.commit()
     print("Tenth value Inserted\n")
     print("All value Inserted into Employees\n")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     print("Initializing Step 3\n")
     print("Creating Mobile_Phones Table\n")
     print("Inserting Values into Mobile_Phones Table")
     cursor.execute("create table Mobile_Phones(Id int primary key, Product_Name varchar(50), Model_Number int, Quantity int, Price int)")
     print("Mobile_Phones Table Created Succesfully")
     print("Inserting Values into Mobile_Phones tables")
     
     cursor.execute("insert into Mobile_Phones values(13001,'Iphone',15,45,107900)")#1
     connection.commit()
     print("First value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13002,'Samsung Galaxy',6,56,99999)")#2
     connection.commit()
     print("Second value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13003,'Vivo',29,34,39999)")#3
     connection.commit()
     print("Third value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13004,'Nokia',42,33,12999)")#4
     connection.commit()
     print("Fourth value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13005,'Gionee',8,37,13990)")#5
     connection.commit()
     print("Fifth value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13006,'BlueBerry',5,77,24900)")#6
     connection.commit()
     print("Sixth value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13007,'Realme',2,46,43999)")#7
     connection.commit()
     print("Seventh value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13008,'Redmi',4,34,29999)")#8
     connection.commit()
     print("Eighth value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13009,'Oppo',4,11,54999)")#9
     connection.commit()
     print("Ninth value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13010,'Lenovo',7,16,59999)")#10
     connection.commit()
     print("Tenth value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13011,'Asus',15,7,89999)")#11
     connection.commit()
     print("Eleventh value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13012,'Motorola',2,12,24999)")#12
     connection.commit()
     print("Twelvth value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13013,'Xiaomi',5,66,22999)")#13
     connection.commit()
     print("Thirteenth value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13014,'OnePlus',8,54,59999)")#14
     connection.commit()
     print("Fourteenth value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13015,'Lava',8,23,7697)")#15
     connection.commit()
     print("Fivteenth value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13016,'Honor',8,66,31998)")#16
     connection.commit()
     print("Sixteenth value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13017,'HTC',5,45,53990)")#17
     connection.commit()
     print("Seventeenth value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13018,'Micromax',7,43,6850)")#18
     connection.commit()
     print("Eighteenth value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13019,'Karbonn',5,23,6499)")#19
     connection.commit()
     print("Ninteenth value Inserted\n")
     cursor.execute("insert into Mobile_Phones values(13020,'Celkon',7,15,5749)")#20
     connection.commit()
     print("Twentyth value Inserted\n")
     print("Mobile_Phones has been Created Succesfully\n")
     print("All Values Inserted Succesfully in Mobile_Phones Table")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     print("Initializing Step 4\n")
     print("Creating Software_Components Table\n")
     print("Inserting Values into Software_Components Table")
     cursor.execute("create table Software_Components(Id int primary key, Product_Name varchar(50), Version int, Quantity int, Price int)")
     print("Software_Components Table Created Succesfully")
     print("Inserting Values into Software_Components tables")
     
     cursor.execute("insert into Software_Components values(19001,'Quick-Heal',15,45,1591)")#1
     connection.commit()
     print("First value Inserted\n")
     cursor.execute("insert into Software_Components values(19002,'AV-NP',6,56,500)")#2
     connection.commit()
     print("Second value Inserted\n")
     cursor.execute("insert into Software_Components values(19003,'360',3,34,664)")#3
     connection.commit()
     print("Third value Inserted\n")
     cursor.execute("insert into Software_Components values(19004,'Cloud Storage',9,33,800)")#4
     connection.commit()
     print("Fourth value Inserted\n")
     cursor.execute("insert into Software_Components values(19005,'CS-GO',8,37,500)")#5
     connection.commit()
     print("Fifth value Inserted\n")
     cursor.execute("insert into Software_Components values(19006,'God-of-war',5,77,999)")#6
     connection.commit()
     print("Sixth value Inserted\n")
     cursor.execute("insert into Software_Components values(19007,'Minecraft',2,46,2500)")#7
     connection.commit()
     print("Seventh value Inserted\n")
     cursor.execute("insert into Software_Components values(19008,'Assassin-Creed',4,34,9862)")#8
     connection.commit()
     print("Eighth value Inserted\n")
     cursor.execute("insert into Software_Components values(19009,'MS-Office',4,11,4589)")#9
     connection.commit()
     print("Ninth value Inserted\n")
     cursor.execute("insert into Software_Components values(19010,'Adobe',7,16,4587)")#10
     connection.commit()
     print("Tenth value Inserted\n")
     cursor.execute("insert into Software_Components values(19011,'Project-standard',15,7,9658)")#11
     connection.commit()
     print("Eleventh value Inserted\n")
     cursor.execute("insert into Software_Components values(19012,'Core-Idraw',2,12,9874)")#12
     connection.commit()
     print("Twelvth value Inserted\n")
     cursor.execute("insert into Software_Components values(19013,'Norton',5,66,999)")#13
     connection.commit()
     print("Thirteenth value Inserted\n")
     cursor.execute("insert into Software_Components values(19014,'Norton-360',8,54,455)")#14
     connection.commit()
     print("Fourteenth value Inserted\n")
     cursor.execute("insert into Software_Components values(19015,'Adobe-Premium',8,23,949)")#15
     connection.commit()
     print("Fivteenth value Inserted\n")
     cursor.execute("insert into Software_Components values(19016,'Folklore',8,66,850)")#16
     connection.commit()
     print("Sixteenth value Inserted\n")
     cursor.execute("insert into Software_Components values(19017,'Among-Us',5,45,450)")#17
     connection.commit()
     print("Seventeenth value Inserted\n")
     cursor.execute("insert into Software_Components values(19018,'Mario-Maker',7,43,300)")#18
     connection.commit()
     print("Eighteenth value Inserted\n")
     cursor.execute("insert into Software_Components values(19019,'Transformers',5,23,2000)")#19
     connection.commit()
     print("Ninteenth value Inserted\n")
     cursor.execute("insert into Software_Components values(19020,'The-Legend-of Zelda',7,15,600)")#20
     connection.commit()
     print("Twentyth value Inserted\n")
     print("Software_Components has been Created Succesfully\n")
     print("All Values Inserted Succesfully in Software_Components Table")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     print("Initializing Step 5\n")
     print("Creating Hardware_Components Table\n")
     print("Inserting Values into Hardware_Components Table")
     cursor.execute("create table Hardware_Components(Id int primary key, Product_Name varchar(50), Version int, Quantity int, Price int)")
     print("Software_Components Table Created Succesfully")
     print("Inserting Values into Hardware_Components tables")
     
     cursor.execute("insert into Hardware_Components values(18001,'Pen-Drive',15,45,449)")#1
     connection.commit()
     print("First value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18002,'Hard-disk',6,56,6149)")#2
     connection.commit()
     print("Second value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18003,'Monitor',3,34,22990)")#3
     connection.commit()
     print("Third value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18004,'Key-Board',9,33,4837)")#4
     connection.commit()
     print("Fourth value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18005,'Mouse',8,37,75377)")#5
     connection.commit()
     print("Fifth value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18006,'Laptop',5,77,73573)")#6
     connection.commit()
     print("Sixth value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18007,'CPU',2,46,25369)")#7
     connection.commit()
     print("Seventh value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18008,'Mother-Board',4,34,75896)")#8
     connection.commit()
     print("Eighth value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18009,'PC-Fan',4,11,25896)")#9
     connection.commit()
     print("Ninth value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18010,'SSD',7,16,14523)")#10
     connection.commit()
     print("Tenth value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18011,'Modem',15,7,75377)")#11
     connection.commit()
     print("Eleventh value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18012,'Router',2,12,37535)")#12
     connection.commit()
     print("Twelvth value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18013,'Ethernet-Cable',5,66,58963)")#13
     connection.commit()
     print("Thirteenth value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18014,'Power-Supply',8,54,14758)")#14
     connection.commit()
     print("Fourteenth value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18015,'Graphics-Card',8,23,36985)")#15
     connection.commit()
     print("Fivteenth value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18016,'Printer',8,66,58963)")#16
     connection.commit()
     print("Sixteenth value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18017,'Control-Unit',5,45,14258)")#17
     connection.commit()
     print("Seventeenth value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18018,'Sound-Board',7,43,35785)")#18
     connection.commit()
     print("Eighteenth value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18019,'Connecting-Wires',5,23,25741)")#19
     connection.commit()
     print("Ninteenth value Inserted\n")
     cursor.execute("insert into Hardware_Components values(18020,'Arduino-Uno',7,15,25896)")#20
     connection.commit()
     print("Twentyth value Inserted\n")
     print("Hardware_Components has been Created Succesfully\n")
     print("All Values Inserted Succesfully in Software_Components Table")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     print("Initializing Step 6\n")
     print("Creating Gadgets Table\n")
     print("Inserting Values into Gadgets Table")
     cursor.execute("create table Gadgets(Id int primary key, Product_Name varchar(50), Version int, Quantity int, Price int)")
     print("Software_Components Table Created Succesfully")
     print("Inserting Values into Gadgets tables")
     
     cursor.execute("insert into Gadgets values(17001,'PowerBank',15,45,90000)")#1
     connection.commit()
     print("First value Inserted\n")
     cursor.execute("insert into Gadgets values(17002,'HeadPhones',6,56,55000)")#2
     connection.commit()
     print("Second value Inserted\n")
     cursor.execute("insert into Gadgets values(17003,'Apple-Watch',3,34,25333)")#3
     connection.commit()
     print("Third value Inserted\n")
     cursor.execute("insert into Gadgets values(17004,'Samsung-Watch',9,33,57355)")#4
     connection.commit()
     print("Fourth value Inserted\n")
     cursor.execute("insert into Gadgets values(17005,'Fit-Bit',8,37,75377)")#5
     connection.commit()
     print("Fifth value Inserted\n")
     cursor.execute("insert into Gadgets values(17006,'Google-Lenses',5,77,73573)")#6
     connection.commit()
     print("Sixth value Inserted\n")
     cursor.execute("insert into Gadgets values(17007,'AirPods',2,46,25369)")#7
     connection.commit()
     print("Seventh value Inserted\n")
     cursor.execute("insert into Gadgets values(17008,'EarPhones',4,34,75896)")#8
     connection.commit()
     print("Eighth value Inserted\n")
     cursor.execute("insert into Gadgets values(17009,'Wireless-HeadPhones',4,11,25896)")#9
     connection.commit()
     print("Ninth value Inserted\n")
     cursor.execute("insert into Gadgets values(17010,'iPad',7,16,14523)")#10
     connection.commit()
     print("Tenth value Inserted\n")
     cursor.execute("insert into Gadgets values(17011,'ipod',15,7,75377)")#11
     connection.commit()
     print("Eleventh value Inserted\n")
     cursor.execute("insert into Gadgets values(17012,'Camera',2,12,37535)")#12
     connection.commit()
     print("Twelvth value Inserted\n")
     cursor.execute("insert into Gadgets values(17013,'Speakes',5,66,58963)")#13
     connection.commit()
     print("Thirteenth value Inserted\n")
     cursor.execute("insert into Gadgets values(17014,'FireTV-Stick',8,54,14758)")#14
     connection.commit()
     print("Fourteenth value Inserted\n")
     cursor.execute("insert into Gadgets values(17015,'Alexa',8,23,36985)")#15
     connection.commit()
     print("Fivteenth value Inserted\n")
     cursor.execute("insert into Gadgets values(17016,'Siri',8,66,58963)")#16
     connection.commit()
     print("Sixteenth value Inserted\n")
     cursor.execute("insert into Gadgets values(17017,'Drone',5,45,14258)")#17
     connection.commit()
     print("Seventeenth value Inserted\n")
     cursor.execute("insert into Gadgets values(17018,'Controller',7,43,35785)")#18
     connection.commit()
     print("Eighteenth value Inserted\n")
     cursor.execute("insert into Gadgets values(17019,'VR-Headset',5,23,25741)")#19
     connection.commit()
     print("Ninteenth value Inserted\n")
     cursor.execute("insert into Gadgets values(17020,'Mac-Book',7,15,25896)")#20
     connection.commit()
     print("Twentyth value Inserted\n")
     print("Gadgets has been Created Succesfully\n")
     print("All Values Inserted Succesfully in Gadgets Table")

     print("All Tables has been created succesfully: ")
     print("You may Procide with your main project")
     print("Thank you")
     connection.close()





def database_2():
     host = input("You Host Name: ")
     user = input("Your User Name: ")
     password = input('Your Password: ')

     try:
               connection_1 = mysql.connector.connect(
                    host = host,
                    user = user,
                    passwd = password
                    )
               cursor_1 = connection_1.cursor()
               if connection_1.is_connected:
                    print("Connection Stablised Succesfully")

     except mysql.connector.Error as s:
               print("Error: {}".format(s))

     cursor_1.execute("show databases like 'Customers'")
     exists = cursor_1.fetchone()

     while True:
          if exists:
               cursor_1.execute("drop database Customers")
               
               cursor_1.execute("create database Customers")
               
               break

          else:
               
               cursor_1.execute("create database Customers")
               
               break

     print("Part 2 Created Succesfully")


instant_setup()
database_2()
     


     
