# import third party python packages
import sys # Imports sys
sys.path.insert(0,'../.') # Sets default sys location
import config # Import config
import pandas as pd # Imports pandas

########################## Create Database on mysql server #####################
def create_db(mysql_user=config.mysql_user, mysql_password=config.mysql_password ,mysql_host=config.mysql_host, db_name=config.db_name): # Gets parameters from user
    # Tries this block of code and looks out for errors
    try:
        conn = MySQLdb.connect(user=mysql_user, host=mysql_host, password=mysql_password) # Connects to mysql database with inputed parameters
        print('Connection to mysql server Done : success')
        # Tries this block of code and looks out for errors
        try:
            cur = conn.cursor() # Creates cursor to write to database
            # Executes task to database and commits it online
            cur.execute("CREATE DATABASE IF NOT EXISTS "+db_name+" ;") 
            conn.commit()
            print("database created with success")
        # Closes connection either ways if something went wrong in code or if everything went right
        finally:
            conn.close()
            print("connection closed !")
    # If anything goes wrong, prints that user can't connect to database
    except:
        print("I am unable to connect to the database")


########################## Create table on mysql server #####################
def create_table(mysql_user=config.mysql_user, mysql_password=config.mysql_password ,mysql_host=config.mysql_host,table_name=config.table_name, db_name=config.db_name): # Gets parameters from user
    # Tries this block of code and looks out for errors
    try:
        conn = MySQLdb.connect(user=mysql_user, host=mysql_host, password=mysql_password,  database=db_name) # Connects to mysql database with inputed parameters
        print('Connection to mysql server Done : success')
        try:
            cur = conn.cursor() # Creates cursor to write to database
            # Executes task to database and commits it online
            # Adds id, email, name and password columns to the table that is created
            cur.execute("""CREATE TABLE IF NOT EXISTS %s (id INT AUTO_INCREMENT PRIMARY KEY,
                                                                              email varchar(250), 
                                                                              name varchar(250),
                                                                              password varchar(250) 
                                                                              );""" %(table_name))
            conn.commit()
            print("Table created with success")
        # Closes connection either ways if something went wrong in code or if everything went right
        finally:
            conn.close()
            print("connection closed !")
    # If anything goes wrong, prints that user can't connect to database
    except:
        print("I am unable to connect to the database")

########################## Inserts row into mysql table #####################
def insert_row(email, name, password, user_name=config.mysql_user, mysql_password=config.mysql_password, host_name=config.mysql_host, db_name=config.db_name, table_name=config.table_name): # Gets parameters from user
    # Define our connection string
    conn = MySQLdb.connect(user=user_name, password=mysql_password, host=host_name, database=db_name) # Connects to mysql database with inputed parameters
    # Tries this block of code and looks out for errors
    try:
        cursor = conn.cursor() # Creates cursor to write to database
        # Executes task to database and commits it online
        # Inserts information about id, email, name and password into table row    
        cursor.execute("""insert into %s (email, name, password) values ('%s', '%s', '%s'); """ %(table_name, email, name, password))
        conn.commit()
    # Closes connection either ways if something went wrong in code or if everything went right
    finally:
        conn.close()
    print('Row inserted')

########################## Imports data from mysql server #####################
def import_data(query, mysql_user=config.mysql_user, mysql_password=config.mysql_password, mysql_host=config.mysql_host): # Gets parameters from user
    # Tries this block of code and looks out for errors
    try:
        conn = MySQLdb.connect(user=mysql_user, host=mysql_host, password=mysql_password) # Connects to mysql database with inputed parameters
        print('Connection to mysql server Done : success')
        print(query)
    # If anything goes wrong, prints that user can't connect to database
    except:
        print("I am unable to connect to the database")
    # Tries this block of code and looks out for errors     
    try:
        cur = conn.cursor() # Creates cursor to write to database
        # Executes task to database and commits it online
        cur.execute(query)
        results = cur.fetchall() # Fetches sql information about data from execution
        data = pd.DataFrame(list(results), columns=[row[0] for row in cur.description]).reset_index(drop=True) # Creates two-dimensional size-mutable table with information from fetch
        print(data) # prints data for testing
    # Closes connection either ways if something went wrong in code or if everything went right
    finally:
        conn.close()
    return (data) # Returns data from function
