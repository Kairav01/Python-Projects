import mysql.connector
from datetime import datetime 

def Mysql_connection():

    print("Welcome to Digital Hub")
    print("what do you want to continue as: ")
    print("1. Employee")
    print("2. Customer")
    a = int(input("Enter your choice: "))

    if a == 1:
        print("Provide us the following details")
        host = input("Enter your Host Name: ")
        user = input("Enter your User Name: ")
        password = input("Enter your Password: ")

        try:
            connection = mysql.connector.connect(
            host = host,
            user = user,
            passwd = password
            )

            cursor = connection.cursor()

            if connection.is_connected:
                print("You have Succesfully Connected to Mysql")
                
        except mysql.connector.Error as Error:
            print('Error: {}',format(Error))

    elif a == 2:
        print("Provide us the following details")
        user = input("Enter your User Name: ")
        password = input("Enter your Password: ")

        try: 
            connection = mysql.connector.connect(
            host = 'localhost',
            user = user,
            passwd = password 
            )
            cursor = connection.cursor()

            if connection.is_connected():
                print("You have logged into Digital Hub")

        except mysql.connector.Error as Error:
            print('Error: {}',format(Error))

    else: 
        print("Invalid Entry Please try again") 
        
Mysql_connection()