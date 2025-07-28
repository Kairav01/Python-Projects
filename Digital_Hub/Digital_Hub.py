import mysql.connector
from datetime import datetime

def Mysql():
     print("****Welcome to Digital Hub****")
     print("What do you want to continue as: ")
     print("1. Employee")
     print("2. Customer")
     print("3. Exit The Program")
     wao = int(input("Type here: "))
#******************************************************************************************************************************************************************************************************************************          
     if wao == 1:
          print('Provoide us the following details')
          host = input("Your Host Name: ")
          user = input("Your User Name: ")
          password = input("Your Password: ")

          try:
               connection = mysql.connector.connect(
                    host = host,
                    user = user,
                    passwd = password
                    )
               cursor = connection.cursor()
               
               if connection.is_connected:
                    print("You have Succesfullly Connected to Mysql")
                    
               while True:
                    print("Do you want to Create a Database or use one")
                    print("1. Create a New Database")
                    print("2. Use an Existing Database")
                    print("3. Exit the Program")
                    c = int(input("Enter your Choice: "))
                    
                    if c == 1:
                         database = input("Enter the Name of the Database: ")
                         cursor.execute('Show databases like "{}"'.format(database))
                         exists = cursor.fetchone()

                         if exists:
                              print("The database \"{}\" already exists\n".format(database))

                         else:
                              cursor.execute("create database {}".format(database))
                              print("The database \"{}\" has been created successfully")
              
                         
                    elif c ==2:
                         print("These are the Existing Databases: ")
                         cursor.execute("show databases")
                         sd = cursor.fetchall()
                         for i in sd:
                              print(i)
                         database = input("Enter the Name of an Existing Database: ")

                            
                    elif c == 3:
                         print("Exiting the Program")
                         break
                    
                    else:
                         print("Invalid Input!! Please Re-Enter your Choice\n")
                         continue
                    
                    
                    connection = mysql.connector.connect(
                         host = host,
                         user = user,
                         passwd = password,
                         database = database
                         )
                    
                    
                    if connection.is_connected:
                         print("You have Succesfully Connected to Mysql database \'{}\'".format(database))
                    cursor = connection.cursor()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    while True:
                         print('\nThese are the following available commands')
                         print('1. Table Creation')
                         print('2. Display Tables')
                         print('3. Insert Details')
                         print('4. Display values')
                         print('5. Update Details')
                         print('6. Delete Details')
                         print('7 Exit the Program\n')
                         print('What command would you like to execute')
                         ce = int(input('Enter your Choice: '))
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                         if ce == 1:              #Table Creation
                              tablename = input("Enter the Name of the New Table: ")
                              cursor.execute('Show Tables like "{}" '.format(tablename))
                              exists = cursor.fetchone()

                              if exists:
                                   print("The Table \"{}\" already exists".format(tablename))

                              else:
                                   while True:
                                        print("\nEnter the name of the column names along with their datatypes")
                                        print("The query should be like: Col.name datatype,Col.name datatype......")
                                        query = input("You may type here: ")

                                        try:
                                             cursor.execute("create table {} ({})".format(tablename,query))
                                             print("The Table\'{}\' has been created Succesfully".format(tablename))

                                        except mysql.connector.Error as Error:
                                             print("Error: {}".format(Error))
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                         elif ce == 2:            #Display Tables
                              print("These are the available tables: ")
                              cursor.execute("Show Tables")
                              for i in cursor:
                                   print(i)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                         elif ce == 3:            #Insert Details
                              print('In which table you want to insert details')
                              print('1. Employees')
                              print('2. Mobile Phones')
                              print('3. Software Components')
                              print('4. Hardware Components')
                              print('5. Gadegts')
                              choice = int(input("Enter you Choice: "))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                              while True:
                                   if choice == 1:
                                        Ename = input("Enter the Name of the Employee: ")
                                        Id = int(input("Enter the Id of the Employee: "))
                                        des = input("Enter the Designation: ")
                                        sal = int(input("Enter the salary for the Employee: "))
                                        query = "insert into Employees value({},'{}','{}',{})".format(Id,Ename,des,sal)
                                        
                                        try:
                                             cursor.execute(query)
                                             connection.commit()
                                             print("These Details has been succesfully uploaded to there designated table")

                                        except mysql.connector.error as Error:
                                             print("Error: {}".format(Error))

                                        break
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                             
                                   elif choice == 2:
                                        Name = input('Enter the Name of the Phone: ')
                                        Id = int(input('Enter the Product ID: '))
                                        Model_Number = int(input("Enter the Model Number: "))
                                        Price = int(input("Enter the price of the Product: "))
                                        quantity = int(input('Enter the total number of product available: '))
                                        query = "insert into Mobile_Phones values({},'{}',{},{},{})".format(Id,Name, Model_Number,quantity,Price)
                                                       
                                        try:
                                             cursor.execute(query)
                                             connection.commit()
                                             print('These Details has been succesfully uploaded to there designated table')

                                        except mysql.connector.error as Error:
                                             print("Error: {}".format(Error))

                                        break
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                   elif choice == 3:
                                        Name = input("Enter the Name of the Software Component: ")
                                        Id = int(input("Enter the Product Id: "))
                                        Version = input("Enter it\'s version")
                                        price = int(input('Enter the Price of the product'))
                                        qty = int(input('Enter the total number of product available: '))
                                        query = "insert into Software_Components values({},'{}',{},{},{})".format(Id,Name,Version,qty,price)

                                        try:
                                             cursor.execute(query)
                                             connection.commit()
                                             print("These Details have been succesfully uploaded to the designated table")

                                        except mysql.connector.error as Error:
                                             print("Error: {}".format(Error))

                                        break
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                   elif choice == 4:
                                        Name = input("Enter the Name of the hardware component: ")
                                        Id = int(input("Enter the Prduct Id: "))
                                        Version = int(input("Enter it\'s version: "))
                                        price = int(input("Enter the Price of the product: "))
                                        qty = int(input('Enter the total number of product available: '))
                                        query = "insert into Hardware_components  values({},'{}',{},{},{})".format(Id,Name,Version,qty,price)

                                        try:
                                             cursor.execute(query)
                                             connection.commit()
                                             print('These Details have been succesfully uploaded to there designated table')

                                        except mysql.connector.error as Error:
                                             print('Error: {}'.format(Error))

                                        break
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                   elif choice == 5:
                                        Name = input("Enter the Name of the Gadget: ")
                                        Id = int(input("Enter the Product ID: "))
                                        Version = int(input('Enter it\'s version'))
                                        price = int(input('Enter the price of the product: '))
                                        qty = int(input("Enter the total number of roduct available: "))
                                        query = "insert into Gadgets values({},'{}',{},{},{})".format(Id,Name,Version,qty,price)

                                        try:
                                             cursor.execute(query)
                                             connection.commit()
                                             print('These Details has been successfully uploaded the there designated table')

                                        except mysql.connector.error as Error:
                                             print("Error: {}".format(Error))

                                        break
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                   
                                   else:
                                        print("Invalid Input!! Please re-enter your choice")
                                        continue
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                         elif  ce == 4:           #Show Details
                              print('Do you want to add any condition to the query: ')
                              print('1. Yes')
                              print('2. No')
                              select = int(input("Enter Your Choice: "))
                              if select == 1:
                                   cursor.execute("Show Tables")
                              
                                   for i in cursor:
                                        print(i)
                                   table = input("Enter the Name of the table that you want to see: ")
                                   cursor.execute("desc {}".format(table))

                                   for i in cursor:
                                        print(i)

                                   condition = input("Enter your condition here: ")
                                   print("This is you table according to your condition")
                                   cursor.execute('select * from {} where {}'.format(table,condition))
                                   for i in cursor:
                                        print(i)

                              elif select == 2:
                                   print("These are the available Tables")
                                   cursor.execute("show tables")

                                   for i in cursor:
                                        print(i)

                                   tables = input("Enter the Name of the table that you want to see: ")
                                   print("This is your Table")
                                   cursor.execute("select  * from {}".format(tables))
                                   
                                   for i in cursor:
                                        print(i)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                         elif ce == 5:            #Update Table 
                              print('Which table would you like to update')
                              print('1. Employees')
                              print('2. Mobile_Phones')
                              print('3. Software_Components')
                              print('4. Hardware_Components')
                              print('5. Gadegts')
                              choice = int(input("Enter your choice: "))
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                              while True:
                                   if choice == 1:                                                  #Updating Employees Table
                                        print("This is the current available table")
                                        cursor.execute("select * from Employees")
                                        emp = cursor.fetchall()
                                        for i in emp:
                                             print(i)
                                        print("\n")
                                        print("Which section would you like to update")
                                        print('1. Designation')
                                        print('2. Salary')
                                        print("This is the Current Table: ")
                                        inner_choice1 = int(input("Enter your choice: "))           
                                        if inner_choice1 == 1:                  #Updating Designation in Employees Table
                                             Id = int(input("Enter the Employee Id: "))
                                             des = input("Enter the employee\'s new designation: ")
                                             query = "update Employees set Designation = '{}' where Employee_Id = {}".format(des, Id)

                                             try:
                                                  cursor.execute(query)
                                                  connection.commit()
                                                  print("The Given detail has been updated")

                                             except mysql.connector.error as Error:
                                                  print('Error: {}'.format(Error))

                                             break
                                        
                                        elif inner_choice1 == 2:                #Updateing Salary in Employees Table
                                             Id = int(input("Enter the Employee\'s ID: "))
                                             sal = int(input("Enter Employees\'s new Id: "))
                                             query = "update Employees set Salary = {} where Employee_Id = {}".format(sal,Id)

                                             try:
                                                  cursor.execute(query)
                                                  connection.commit()
                                                  print('The Given detail has been updated')

                                             except mysql.connector.Error as s:
                                                  print("Error: {}".format(s))

                                             break
                                        else:
                                             print("Invalid Choice!! Please re-enter")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                   elif choice == 2:                                                  #Updating Mobile Phones Table
                                        print("These are the current available details: ")
                                        cursor.execute('select * from Mobile_Phones')
                                        mp = cursor.fetchall()
                                        for i in mp:
                                             print(i)
                                        print("\n")
                                        print("Which Section would you like to update?")
                                        print("Model Number")
                                        print('Quantity')
                                        print('Price')
                                        inner_choice2 = int(input('Enter your Choice: '))
                                        while True:
                                             if inner_choice2 == 1:             #Updating Model Number in Mobile Phones Table
                                                  Id = int(input("Enter the Mobile Id: "))
                                                  Model_number = int(input("Enter the New Model Number for the Mobile\'s Id- {}: ".format(Id)))
                                                  query = "update Mobile_Phones set Model_Number = {} where Id = {}".format(Model_Number,Id)

                                                  try:
                                                       cursor.execute(query)
                                                       connection.commit()
                                                       print("The Given Detail has been updated")

                                                  except mysql.connector.Error as Error:
                                                       print("Error: {}".format(Error))

                                                  break

                                             elif inner_choice2 == 2:           #Updating Quantity in Mobile Phones Table
                                                  Id = int(input('Enter the Mobile Id: '))
                                                  Quantity = int(input('Enter the New Quantity for the Mobile\'s Id- {}: '.format(Id)))
                                                  query = "update Mobile_Phones set Quantity = {} where Id = {}".format(Quantity,Id)

                                                  try:
                                                       cursor.execute(query)
                                                       connection.commit()
                                                       print("The Given Detail has been Updated")

                                                  except mysql.connector.Error as Error:
                                                       print("Error: {}".format(Error))

                                                  break

                                             elif inner_choice2 == 3:           #updating Price in Mobile Phones Table
                                                  Id = int(input('Enter the Mobile Id: '))
                                                  Price = int(input('Enter the New Price for the Mobile\'s Id- {}: '.format(Id)))
                                                  query = "update Mobile_Phones set Price = {} where Id = {}".format(Price,Id)

                                                  try:
                                                       cursor.execute(query)
                                                       connection.commit()
                                                       print('The Given Detail has been Updated')

                                                  except mysql.connector.Error as s:
                                                       print("Error: {}".format(s))

                                                  break

                                             else:
                                                  print("Invalid Input!! Please Re-enter ")
                                                  continue
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                   elif choice == 3:                                                  #Updating Software_Components Table
                                        print("These are the current available details: ")
                                        cursor.execute('select * from Software_Components')
                                        sc = cursor.fetchall()
                                        for i in sc:
                                             print(i)
                                        print("\n")
                                        print("Which Section would you like to update?")
                                        print("Model Number")
                                        print('Quantity')
                                        print('Price')
                                        inner_choice3 = int(input('Enter your Choice: '))
                                        while True:
                                             if inner_choice3 == 1:             #Updating Version in Software_Components Table
                                                  Id = int(input("Enter the Mobile Id: "))
                                                  Version = int(input("Enter the New Version for the Software_Component\'s Id- {}: ".format(Id)))
                                                  query = "update Software_Components set Version = {} where Id = {}".format(Model_Number,Id)

                                                  try:
                                                       cursor.execute(query)
                                                       connection.commit()
                                                       print("The Given Detail has been updated")

                                                  except mysql.connector.Error as Error:
                                                       print("Error: {}".format(Error))

                                                  break

                                             elif inner_choice3 == 2:           #Updating Quantity in Software_Componets Table
                                                  Id = int(input('Enter the Mobile Id: '))
                                                  Quantity = int(input('Enter the New Quantity for the Software_Component\'s Id- {}: '.format(Id)))
                                                  query = "update Software_Components set Quantity = {} where Id = {}".format(Quantity,Id)

                                                  try:
                                                       cursor.execute(query)
                                                       connection.commit()
                                                       print("The Given Detail has been Updated")

                                                  except mysql.connector.Error as Error:
                                                       print("Error: {}".format(Error))

                                                  break

                                             elif inner_choice3 == 3:           #updating Price in Software_Components Table
                                                  Id = int(input('Enter the Mobile Id: '))
                                                  Price = int(input('Enter the New Price for the Software_Component\'s Id- {}: '.format(Id)))
                                                  query = "update Software_Components set Price = {} where Id = {}".format(Price,Id)

                                                  try:
                                                       cursor.execute(query)
                                                       connection.commit()
                                                       print('The Given Detail has been Updated')

                                                  except mysql.connector.Error as s:
                                                       print("Error: {}".format(s))

                                                  break

                                             else:
                                                  print("Invalid Input!! Please Re-enter ")
                                                  continue
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                        
                                   elif choice == 4:                                                  #Updating Hardware_Components Table
                                        print("These are the current available details: ")
                                        cursor.execute('select * from Hardware_Components')
                                        hc = cursor.fetchall()
                                        for i in hc:
                                             print(i)
                                        print("\n")
                                        print("Which Section would you like to update?")
                                        print("Model Number")
                                        print('Quantity')
                                        print('Price')
                                        inner_choice4 = int(input('Enter your Choice: '))
                                        while True:
                                             if inner_choice4 == 1:             #Updating Version in Hardware_Components Table
                                                  Id = int(input("Enter the Mobile Id: "))
                                                  Version = int(input("Enter the New Version for the Hardware_Components\'s Id- {}: ".format(Id)))
                                                  query = "update Hardware_Components set Version = {} where Id = {}".format(Model_Number,Id)

                                                  try:
                                                       cursor.execute(query)
                                                       cursor.commit()
                                                       print("The Given Detail has been updated")

                                                  except mysql.connector.Error as Error:
                                                       print("Error: {}".format(Error))

                                                  break

                                             elif inner_choice4 == 2:           #Updating Quantity in Hardware_Componets Table
                                                  Id = int(input('Enter the Mobile Id: '))
                                                  Quantity = int(input('Enter the New Quantity for the Hardware_Components\'s Id- {}: '.format(Id)))
                                                  query = "update Hardware_Components set Quantity = {} where Id = {}".format(Quantity,Id)

                                                  try:
                                                       cursor.execute(query)
                                                       connection.commit()
                                                       print("The Given Detail has been Updated")

                                                  except mysql.connector.Error as Error:
                                                       print("Error: {}".format(Error))

                                                  break

                                             elif inner_choice4 == 3:           #updating Price in Hardware_Components Table
                                                  Id = int(input('Enter the Mobile Id: '))
                                                  Price = int(input('Enter the New Price for the Hardware_Components\'s Id- {}: '.format(Id)))
                                                  query = "update Hardware_Components set Price = {} where Id = {}".format(Price,Id)

                                                  try:
                                                       cursor.execute(query)
                                                       connection.commit()
                                                       print('The Given Detail has been Updated')

                                                  except mysql.connector.Error as s:
                                                       print("Error: {}".format(s))

                                                  break

                                             else:
                                                  print("Invalid Input!! Please Re-enter ")
                                                  continue    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                        
                                   elif choice == 5:                                                  #Updating Gadgets Table
                                        print("These are the current available details: ")
                                        cursor.execute('select * from Gadgets')
                                        g = cursor.fetchall()
                                        for i in g:
                                             print(i)
                                        print("\n")
                                        print("Which Section would you like to update?")
                                        print("Model Number")
                                        print('Quantity')
                                        print('Price')
                                        inner_choice5 = int(input('Enter your Choice: '))
                                        while True:
                                             if inner_choice5 == 1:             #Updating Version in Gadgets Table
                                                  Id = int(input("Enter the Mobile Id: "))
                                                  Version = int(input("Enter the New Version for the Gadgets\'s Id- {}: ".format(Id)))
                                                  query = "update Gadgets set Version = {} where Id = {}".format(Model_Number,Id)

                                                  try:
                                                       cursor.execute(query)
                                                       connection.commit()
                                                       print("The Given Detail has been updated")

                                                  except mysql.connector.Error as Error:
                                                       print("Error: {}".format(Error))

                                                  break

                                             elif inner_choice5 == 2:           #Updating Quantity in Gadgets Table
                                                  Id = int(input('Enter the Mobile Id: '))
                                                  Quantity = int(input('Enter the New Quantity for the Gadgets\'s Id- {}: '.format(Id)))
                                                  query = "update Gadgets set Quantity = {} where Id = {}".format(Quantity,Id)

                                                  try:
                                                       cursor.execute(query)
                                                       connection.commit()
                                                       print("The Given Detail has been Updated")

                                                  except mysql.connector.Error as Error:
                                                       print("Error: {}".format(Error))

                                                  break

                                             elif inner_choice5 == 3:           #updating Price in Gadgets Table
                                                  Id = int(input('Enter the Mobile Id: '))
                                                  Price = int(input('Enter the New Price for the Gadgets\'s Id- {}: '.format(Id)))
                                                  query = "update Gadgets set Price = {} where Id = {}".format(Price,Id)

                                                  try:
                                                       cursor.execute(query)
                                                       connection.commit()
                                                       print('The Given Detail has been Updated')

                                                  except mysql.connector.Error as s:
                                                       print("Error: {}".format(s))

                                                  break

                                             else:
                                                  print("Invalid Input!! Please Re-enter ")
                                                  continue
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                        
                                   else:
                                        print("Invalid Input!! Please re-enter your choice")
                                        continue
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                         elif ce == 6:            #Delete Details
                              print('These are the available table: ')
                              print("1. Employees")
                              print("2. Mobile Phones")
                              print("3. Software Components")
                              print("4. Hardware Components")
                              print("5. Gadgets")
                              selection = int(input("Enter your Choice: "))
                              while True:
                                   if selection == 1:
                                        Id = int(input('Enter the Employee\'s Id: '))
                                        query = "delete from Employees where Id = {}".format(Id)
                                        try:
                                             cursor.execute(query)
                                             connection.commit()
                                             print("The Person Has Been Removed from Job")

                                        except mysql.connector.Error as a:
                                             print("Error: {}".format(a))

                                        break
                                   elif selection == 2:
                                        Id = int(input('Enter the Mobile_Phone\'s Id: '))
                                        query = "delete from Mobile_Phones where Id = {}".format(Id)
                                        try:
                                             cursor.execute(query)
                                             connection.commit()
                                             print("This Product has been removed from the Store")

                                        except mysql.connector.Error as a:
                                             print("Error: {}".format(a))

                                        break

                                   elif selection == 3:
                                        Id = int(input('Enter the Software_Component\'s Id: '))
                                        query = "delete from Software_Component where Id = {}".format(Id)
                                        try:
                                             cursor.execute(query)
                                             connection.commit()
                                             print("This Product has been removed from the Store")

                                        except mysql.connector.Error as a:
                                             print("Error: {}".format(a))

                                        break
                                   elif selection == 4:
                                        Id = int(input('Enter the Hardware_Component\'s Id: '))
                                        query = "delete from Hardware_Component where Id = {}".format(Id)
                                        try:
                                             cursor.execute(query)
                                             connection.commit()
                                             print("This Product has been removed from the Store")

                                        except mysql.connector.Error as a:
                                             print("Error: {}".format(a))

                                        break
                              
                                   elif selection == 5:
                                        Id = int(input('Enter the Gadget\'s Id: '))
                                        query = "delete from Gadget where Id = {}".format(Id)
                                        try:
                                             cursor.execute(query)
                                             connection.commit()
                                             print("This Product has been removed from the Store")

                                        except mysql.connector.Error as a:
                                              print("Error: {}".format(a))

                                        break
                                             
                                   else:
                                        print("Invalid Entry!! Please Re-enter")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                         elif ce == 7:
                              print("Disconnecting from Database")
                              break
          

          except mysql.connector.Error as Error:
               print("Error: {}".format(Error))

          finally:
               if 'connection' in locals() and connection.is_connected():
                    print("Mysql Connection is closed")
                    connection.close()
#******************************************************************************************************************************************************************************************************************************                                        
     elif wao == 2:
          print("Provide us the following details: ")
          user = input('Enter your User Name: ')
          passwd = input("Enter you Password: ")

          try:
               connection_1 = mysql.connector.connect(
                    host = "localhost",
                    user = user,
                    passwd = passwd,
                    database = "customers"
                    )
               cursor_1 = connection_1.cursor()

               if connection_1.is_connected():
                    print("Hello")

          except mysql.connector.Error as Error:
               print("Error: {}".format(Error))

          try:
               connection = mysql.connector.connect(
                    host = "localhost",
                    user = user,
                    passwd = passwd,
                    database = "digital_hub"
                    )
               cursor = connection.cursor()

               if connection.is_connected:
                    print("Welcome to Digital Hub")
               Name = input("We would like to know your name: ")
               cursor.execute("show tables like '{}'".format(Name))
               exists = cursor.fetchone()

               cursor_1.execute("show tables like '{}'".format(Name))
               exists_1 = cursor_1.fetchone()

               while True:
                    if exists_1:
                         break
                    else:
                         query_1 = ("create table {} (Purchase_Date date, Product_Name varchar(50), Quantity int, Product_Price int)".format(Name))
                         cursor_1.execute(query_1)
                         break
               
               while True:
                    if exists:
                         print("Carefull You have an Existing Cart: ")
                         print("Do you want to Continue with it: ")
                         print('1. Yes')
                         print('2. No')
                         dog = int(input("Enter your Choice: "))
                         if dog == 1:
                              break
                                                                     
                         elif dog == 2:
                              cursor.execute("drop table {}".format(Name))
                              cursor.execute("create table {} (Product_Id int,Product_Name varchar(50), Price int, Quantity int)".format(Name))
                              break
                              
                    else:
                         cursor.execute("create table {} (Product_Id int,Product_Name varchar(50), Price int, Quantity int)".format(Name))
                         break
               

          
               while True:
     
                    print("What would you like to buy: ")
                    print("1. Mobile Phones")
                    print("2. Software Components")
                    print("3. Hardware Components")
                    print("4. Gadgets")
                    customer = int(input('Enter your choice: '))
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                    
                    if customer == 1:
                         print("These are the available Mobile Phones in the store: ")
                         cursor.execute("select * from Mobile_Phones")
                         mp = cursor.fetchall()
                         for i in mp:
                              print(i)

                         Id = int(input("Enter the Product Id that you want to buy: "))
                         cursor.execute('select Quantity from Mobile_Phones where Id = {}'.format(Id))
                         eq = cursor.fetchone()
                         exists = cursor.rowcount > 0

                         if exists and eq[0] != 0:
                              print("This is your product")
                              cursor.execute('select * from Mobile_Phones where Id = {}'.format(Id))
                              a = cursor.fetchone()
                              print(a)
                              
                              
                              cursor.execute("select Product_Name from Mobile_Phones where Id = {}".format(Id))
                              pn = cursor.fetchone()
                              ProductName1 = pn[0]
                              cursor.execute("select Price from Mobile_Phones where Id = {}".format(Id))
                              p =  cursor.fetchone()
                              price = p[0]
                              quantity = int(input("How many {} would you like to buy: ".format(ProductName1)))

                              cursor.execute("select Product_Name from {} where Product_Name = '{}'".format(Name,ProductName1))
                              alpha = cursor.fetchone()

                              if alpha:
                                   print("This product already Exists in your cart. What would you like to do: ")
                                   print("1. Add the Quantities: ")
                                   print("2. Replace the current Quantity with the Old Quantity: ")
                                   disk = int(input("Enter your Choice: "))
                              
                                   while True:

                                        if disk == 1:
                                             cursor.execute("select Quantity from {} where Product_Name = '{}'".format(Name,ProductName1))
                                             pulse = cursor.fetchone()
                                             pack = pulse[0]
                                             ppulse = pack + quantity
                                             
                                             cursor.execute("select Quantity from Mobile_Phones where Product_Name = '{}'".format(ProductName1))
                                             package = cursor. fetchone()
                                             packet = package[0]
                                             
                                             if ppulse > packet:
                                                  print("We do not have \"{}\" number of {}".format(ppulse,ProductName1))
                                                  print("Please Re-consider the Quantity or Look for another Phone" )
                                                  break
                                             
                                             elif ppulse == packet:
                                                  print("Your Cart have been updated: ")     
                                                  cursor.execute("update {} set Quantity = {} where Product_Name = '{}'".format(Name,ppulse,ProductName1))
                                                  connection.commit()
                                                  break
                                             
                                             else:
                                                  print("Your Cart have been updated: ")     
                                                  cursor.execute("update {} set Quantity = {} where Product_Name = '{}'".format(Name,ppulse,ProductName1))
                                                  connection.commit()
                                                  break

                                        elif disk == 2:
                                             cursor.execute("select Quantity from Mobile_Phones where Product_Name = '{}'".format(ProductName1))
                                             package = cursor.fetchone()
                                             packet = package[0]
                                             
                                             if quantity > packet:
                                                  print("We do not have \"{}\" number of {}".format(ppulse,ProductName1))
                                                  print("Please Re-consider the Quantity or Look for another Phone" )
                                                  break
                                             
                                             elif quantity == packet:
                                                  print("Your Cart have been updated: ")     
                                                  cursor.execute("update {} set Quantity = {} where Product_Name = '{}'".format(Name,quantity,ProductName1))
                                                  connection.commit()
                                                  break
                                             
                                             else:
                                                  print("Your Cart have been updated: ")     
                                                  cursor.execute("update {} set Quantity = {} where Product_Name = '{}'".format(Name,quantity,ProductName1))
                                                  connection.commit()
                                                  break

                                        else:
                                             print('Invalid Entry!! Please Re-enter')
                                             continue
                                        
                              else:
                                   cursor.execute("insert into {} values({}, '{}', {}, {})".format(Name, Id, ProductName1, price, quantity))
                                   connection.commit()
                              
                         else:
                              print("This Product is currently not available")

                         print("Do you want to continue Shopping")
                         print("1. Yes")
                         print("2. No")
                         continue1 = int(input("Enter Your Choice: "))
                         if continue1 == 1:
                              continue
                         elif continue1 ==2:
                              break
                         else:
                              print("Invalid Input!! Please Re-enter")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    elif customer == 2:
                         print("These are the available Software Components in the store: ")
                         cursor.execute("select * from Software_Components")
                         mp = cursor.fetchall()
                         for i in mp:
                              print(i)

                         Id = int(input("Enter the Product Id that you want to buy: "))
                         cursor.execute('select Quantity from Software_Components where Id = {}'.format(Id))
                         eq = cursor.fetchone()
                         exists = cursor.rowcount > 0

                         if exists and eq[0] != 0:
                              print("This is your product")
                              cursor.execute('select * from Software_Components where Id = {}'.format(Id))
                              a = cursor.fetchone()
                              print(a)
                              
                              
                              cursor.execute("select Product_Name from Software_Components where Id = {}".format(Id))
                              pn = cursor.fetchone()
                              ProductName1 = pn[0]
                              cursor.execute("select Price from Software_Components where Id = {}".format(Id))
                              p =  cursor.fetchone()
                              price = p[0]
                              quantity = int(input("How many {} would you like to buy: ".format(ProductName1)))

                              cursor.execute("select Product_Name from {} where Product_Name = '{}'".format(Name,ProductName1))
                              alpha = cursor.fetchone()

                              if alpha:
                                   print("This product already Exists in your cart. What would you like to do: ")
                                   print("1. Add the Quantities: ")
                                   print("2. Replace the current Quantity with the Old Quantity: ")
                                   disk = int(input("Enter your Choice: "))
                              
                                   while True:

                                        if disk == 1:
                                             cursor.execute("select Quantity from {} where Product_Name = '{}'".format(Name,ProductName1))
                                             pulse = cursor.fetchone()
                                             pack = pulse[0]
                                             ppulse = pack + quantity
                                             
                                             cursor.execute("select Quantity from Software_Components where Product_Name = '{}'".format(ProductName1))
                                             package = cursor. fetchone()
                                             packet = package[0]
                                             
                                             if ppulse > packet:
                                                  print("We do not have \"{}\" number of {}".format(ppulse,ProductName1))
                                                  print("Please Re-consider the Quantity or Look for another Software_Components" )
                                                  break
                                             
                                             elif ppulse == packet:
                                                  print("Your Cart have been updated: ")     
                                                  cursor.execute("update {} set Quantity = {} where Product_Name = '{}'".format(Name,ppulse,ProductName1))
                                                  connection.commit()
                                                  break
                                             
                                             else:
                                                  print("Your Cart have been updated: ")     
                                                  cursor.execute("update {} set Quantity = {} where Product_Name = '{}'".format(Name,ppulse,ProductName1))
                                                  connection.commit()
                                                  break

                                        elif disk == 2:
                                             cursor.execute("select Quantity from Software_Components where Product_Name = '{}'".format(ProductName1))
                                             package = cursor.fetchone()
                                             packet = package[0]
                                             
                                             if quantity > packet:
                                                  print("We do not have \"{}\" number of {}".format(ppulse,ProductName1))
                                                  print("Please Re-consider the Quantity or Look for another Software Components" )
                                                  break
                                             
                                             elif quantity == packet:
                                                  print("Your Cart have been updated: ")     
                                                  cursor.execute("update {} set Quantity = {} where Product_Name = '{}'".format(Name,quantity,ProductName1))
                                                  connection.commit()
                                                  break
                                             
                                             else:
                                                  print("Your Cart have been updated: ")     
                                                  cursor.execute("update {} set Quantity = {} where Product_Name = '{}'".format(Name,quantity,ProductName1))
                                                  connection.commit()
                                                  break

                                        else:
                                             print('Invalid Entry!! Please Re-enter')
                                             continue
                                        
                              else:
                                   cursor.execute("insert into {} values({}, '{}', {}, {})".format(Name, Id, ProductName1, price, quantity))
                                   connection.commit()
                              
                         else:
                              print("This Product is currently not available")

                         print("Do you want to continue Shopping")
                         print("1. Yes")
                         print("2. No")
                         continue1 = int(input("Enter Your Choice: "))
                         if continue1 == 1:
                              continue
                         elif continue1 ==2:
                              break
                         else:
                              print("Invalid Input!! Please Re-enter")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    elif customer == 3:
                         print("These are the available Hardware Components in the store: ")
                         cursor.execute("select * from Hardware_Components")
                         mp = cursor.fetchall()
                         for i in mp:
                              print(i)

                         Id = int(input("Enter the Product Id that you want to buy: "))
                         cursor.execute('select Quantity from Hardware_Components where Id = {}'.format(Id))
                         eq = cursor.fetchone()
                         exists = cursor.rowcount > 0

                         if exists and eq[0] != 0:
                              print("This is your product")
                              cursor.execute('select * from Hardware_Components where Id = {}'.format(Id))
                              a = cursor.fetchone()
                              print(a)
                              
                              
                              cursor.execute("select Product_Name from Hardware_Components where Id = {}".format(Id))
                              pn = cursor.fetchone()
                              ProductName1 = pn[0]
                              cursor.execute("select Price from Hardware_Components where Id = {}".format(Id))
                              p =  cursor.fetchone()
                              price = p[0]
                              quantity = int(input("How many {} would you like to buy: ".format(ProductName1)))

                              cursor.execute("select Product_Name from {} where Product_Name = '{}'".format(Name,ProductName1))
                              alpha = cursor.fetchone()

                              if alpha:
                                   print("This product already Exists in your cart. What would you like to do: ")
                                   print("1. Add the Quantities: ")
                                   print("2. Replace the current Quantity with the Old Quantity: ")
                                   disk = int(input("Enter your Choice: "))
                              
                                   while True:

                                        if disk == 1:
                                             cursor.execute("select Quantity from {} where Product_Name = '{}'".format(Name,ProductName1))
                                             pulse = cursor.fetchone()
                                             pack = pulse[0]
                                             ppulse = pack + quantity
                                             
                                             cursor.execute("select Quantity from Hardware_Components where Product_Name = '{}'".format(ProductName1))
                                             package = cursor. fetchone()
                                             packet = package[0]
                                             
                                             if ppulse > packet:
                                                  print("We do not have \"{}\" number of {}".format(ppulse,ProductName1))
                                                  print("Please Re-consider the Quantity or Look for another Hardware Components" )
                                                  break
                                             
                                             elif ppulse == packet:
                                                  print("Your Cart have been updated: ")     
                                                  cursor.execute("update {} set Quantity = {} where Product_Name = '{}'".format(Name,ppulse,ProductName1))
                                                  connection.commit()
                                                  break
                                             
                                             else:
                                                  print("Your Cart have been updated: ")     
                                                  cursor.execute("update {} set Quantity = {} where Product_Name = '{}'".format(Name,ppulse,ProductName1))
                                                  connection.commit()
                                                  break

                                        elif disk == 2:
                                             cursor.execute("select Quantity from Hardware_Components where Product_Name = '{}'".format(ProductName1))
                                             package = cursor.fetchone()
                                             packet = package[0]
                                             
                                             if quantity > packet:
                                                  print("We do not have \"{}\" number of {}".format(ppulse,ProductName1))
                                                  print("Please Re-consider the Quantity or Look for another Hardware Components" )
                                                  break
                                             
                                             elif quantity == packet:
                                                  print("Your Cart have been updated: ")     
                                                  cursor.execute("update {} set Quantity = {} where Product_Name = '{}'".format(Name,quantity,ProductName1))
                                                  connection.commit()
                                                  break
                                             
                                             else:
                                                  print("Your Cart have been updated: ")     
                                                  cursor.execute("update {} set Quantity = {} where Product_Name = '{}'".format(Name,quantity,ProductName1))
                                                  connection.commit()
                                                  break

                                        else:
                                             print('Invalid Entry!! Please Re-enter')
                                             continue
                                        
                              else:
                                   cursor.execute("insert into {} values({}, '{}', {}, {})".format(Name, Id, ProductName1, price, quantity))
                                   connection.commit()
                              
                         else:
                              print("This Product is currently not available")

                         print("Do you want to continue Shopping")
                         print("1. Yes")
                         print("2. No")
                         continue1 = int(input("Enter Your Choice: "))
                         if continue1 == 1:
                              continue
                         elif continue1 ==2:
                              break
                         else:
                              print("Invalid Input!! Please Re-enter")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    elif customer == 4:
                         print("These are the available Gadgets in the store: ")
                         cursor.execute("select * from Gadgets")
                         mp = cursor.fetchall()
                         for i in mp:
                              print(i)

                         Id = int(input("Enter the Product Id that you want to buy: "))
                         cursor.execute('select Quantity from Gadgets where Id = {}'.format(Id))
                         eq = cursor.fetchone()
                         exists = cursor.rowcount > 0

                         if exists and eq[0] != 0:
                              print("This is your product")
                              cursor.execute('select * from Gadgets where Id = {}'.format(Id))
                              a = cursor.fetchone()
                              print(a)
                              
                              
                              cursor.execute("select Product_Name from Gadgets where Id = {}".format(Id))
                              pn = cursor.fetchone()
                              ProductName1 = pn[0]
                              cursor.execute("select Price from Gadgets where Id = {}".format(Id))
                              p =  cursor.fetchone()
                              price = p[0]
                              quantity = int(input("How many {} would you like to buy: ".format(ProductName1)))

                              cursor.execute("select Product_Name from {} where Product_Name = '{}'".format(Name,ProductName1))
                              alpha = cursor.fetchone()

                              if alpha:
                                   print("This product already Exists in your cart. What would you like to do: ")
                                   print("1. Add the Quantities: ")
                                   print("2. Replace the current Quantity with the Old Quantity: ")
                                   disk = int(input("Enter your Choice: "))
                              
                                   while True:

                                        if disk == 1:
                                             cursor.execute("select Quantity from {} where Product_Name = '{}'".format(Name,ProductName1))
                                             pulse = cursor.fetchone()
                                             pack = pulse[0]
                                             ppulse = pack + quantity
                                             
                                             cursor.execute("select Quantity from Gadgets where Product_Name = '{}'".format(ProductName1))
                                             package = cursor. fetchone()
                                             packet = package[0]
                                             
                                             if ppulse > packet:
                                                  print("We do not have \"{}\" number of {}".format(ppulse,ProductName1))
                                                  print("Please Re-consider the Quantity or Look for another Phone" )
                                                  break
                                             
                                             elif ppulse == packet:
                                                  print("Your Cart have been updated: ")     
                                                  cursor.execute("update {} set Quantity = {} where Product_Name = '{}'".format(Name,ppulse,ProductName1))
                                                  connection.commit()
                                                  break
                                             
                                             else:
                                                  print("Your Cart have been updated: ")     
                                                  cursor.execute("update {} set Quantity = {} where Product_Name = '{}'".format(Name,ppulse,ProductName1))
                                                  connection.commit()
                                                  break

                                        elif disk == 2:
                                             cursor.execute("select Quantity from Gadgets where Product_Name = '{}'".format(ProductName1))
                                             package = cursor.fetchone()
                                             packet = package[0]
                                             
                                             if quantity > packet:
                                                  print("We do not have \"{}\" number of {}".format(ppulse,ProductName1))
                                                  print("Please Re-consider the Quantity or Look for another Phone" )
                                                  break
                                             
                                             elif quantity == packet:
                                                  print("Your Cart have been updated: ")     
                                                  cursor.execute("update {} set Quantity = {} where Product_Name = '{}'".format(Name,quantity,ProductName1))
                                                  connection.commit()
                                                  break
                                             
                                             else:
                                                  print("Your Cart have been updated: ")     
                                                  cursor.execute("update {} set Quantity = {} where Product_Name = '{}'".format(Name,quantity,ProductName1))
                                                  connection.commit()
                                                  break

                                        else:
                                             print('Invalid Entry!! Please Re-enter')
                                             continue
                                        
                              else:
                                   cursor.execute("insert into {} values({}, '{}', {}, {})".format(Name, Id, ProductName1, price, quantity))
                                   connection.commit()
                              
                         else:
                              print("This Product is currently not available")

                         print("Do you want to continue Shopping")
                         print("1. Yes")
                         print("2. No")
                         continue1 = int(input("Enter Your Choice: "))
                         if continue1 == 1:
                              continue
                         elif continue1 ==2:
                              break
                         else:
                              print("Invalid Input!! Please Re-enter")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                  
                    else:
                         print("Invalid Input!! Please Re-Enter")

                         


               cursor.execute("delete from {} where Quantity = 0".format(Name))
               connection.commit()
                         
               cursor.execute("show tables like '{}'".format(Name))
               exists = cursor.fetchone()
               if exists: 
                    print("Hello, ")
                    while True:
                         N = int(input("Please Enter you Phone Number: "))
                         s = str(N)
                         if s.isdigit() and len(s) == 10:
                              break
                         elif len(s) > 10 or len(s) < 10:
                              print("Invalid Number Please Re-Enter")
                              
                    
                    print("This is your Cart")
                    cursor.execute("select * from {}".format(Name))
                    cart = cursor.fetchall()
                    for i in cart:
                        print(i)
                    cursor.execute("select sum((Price*Quantity*0.18)+(Price*Quantity)) from {}".format(Name))
                    b = cursor.fetchone()
                    bill = b[0]
                    
                    print("Your Total Bill is: $",bill)
                    print('Thank you for Shopping from our Store')

                    cursor.execute("insert into Customers values('{}',{},{})".format(Name,N,bill))
                    connection.commit()

                    cursor.execute("select Product_Id,Quantity from {}".format(Name))
                    products = cursor.fetchall()
                    
                    for i in products:
                         pro = i[0]
                         q = i[1]
                         p = str(i[0])
                         
                         if p[:2] == '13':
                              cursor.execute("select Quantity from Mobile_Phones where Id = {}".format(pro))
                              result = cursor.fetchone()
                              
                              if result:
                                   current_quantity = result[0]
                                   new_quantity = current_quantity - q
                                   query = "update Mobile_Phones set Quantity = {} where Id = {}".format(new_quantity,pro)

                                   try:
                                        cursor.execute(query)
                                        connection.commit()

                                   except mysql.connector.Error as s:
                                        print("Error: {}".format(s))

                         elif p[:2] == '19':
                              cursor.execute("select Quantity from Software_Components where Id = {}".format(pro))
                              result = cursor.fetchone()

                              if result:
                                   current_quantity = result[0]
                                   new_quantity = current_quantity - q
                                   query = "update Software_Components set Quantity = {} where Id = {}".format(new_quantity,pro)

                                   try:
                                        cursor.execute(query)
                                        connection.commit()

                                   except mysql.connector.Error as s:
                                        print("Error: {}".format(s))

                         elif p[:2] == '18':
                              cursor.execute("select Quantity from Hardware_Components where Id = {}".format(pro))
                              result = cursor.fetchone()

                              if result:
                                   current_quantity = result[0]
                                   new_quantity = current_quantity - q
                                   query = "update Hardware_Components set Quantity = {} where Id = {}".format(new_quantity,pro)

                                   try:
                                        cursor.execute(query)
                                        connection.commit()

                                   except mysql.connector.Error as s:
                                        print("Error: {}".format(s))

                         elif p[:2] == '17':
                              cursor.execute("select Quantity from Gadgets where Id = {}".format(pro))
                              result = cursor.fetchone()

                              if result:
                                   current_quantity = result[0]
                                   new_quantity = current_quantity - q
                                   query = "update Gadgets set Quantity = {} where Id = {}".format(new_quantity,pro)

                                   try:
                                        cursor.execute(query)
                                        connection.commit()

                                   except mysql.connector.Error as s:
                                        print("Error: {}".format(s))

                    current_datetime = datetime.now()
                                       
                    cursor_1.execute("show tables like '{}'".format(Name))
                    exisits = cursor_1.fetchone()
                    while True:
                         if exisits:
                              cursor.execute("select * from {}".format(Name))
                              dawn = cursor.fetchall()

                              for i in dawn:
                                   product_date = current_datetime.date()
                                   product_name = i[1]
                                   quantity = i[3]
                                   price = i[2]
                                   cursor_1.execute("insert into {} values('{}','{}',{},{})".format(Name, product_date,product_name,quantity,price))
                                   connection_1.commit()
                              break
                         else:
                              break
        
                    cursor.execute("drop table {}".format(Name))

               else:          
                    print("Your Cart is still Empty")
                     
          except mysql.connector.Error as s:
               print('Error: {}'.format(s))

          finally:
               if 'connection' in locals() and connection.is_connected():
                    print("Mysql Connection is closed")
                    connection.close()
                    connection_1.close()

          
#******************************************************************************************************************************************************************************************************************************         
     elif wao == 3:
          print('Exiting the Program')
Mysql()
