#!/usr/bin/python3

import psycopg2
import sys

config = {}

# Helper functions to print texts in different colors
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 

# Function to get database connection details 
def getDbData():
    try : 
        prCyan("Enter host name or press ENTER for localhost : ")
        config['host'] = input()
        if config['host'] == "": config['host'] = "localhost"
        prCyan("Enter port number or press ENTER for using port '5432' : ")
        config['port'] = input()
        if config['port'] == "": config['port'] = "5432"
        prCyan("Enter database name : ")
        config['database'] = input()
        prCyan("Enter user name : ")
        config['user'] = input()
        prCyan("Enter password : ")
        config['password'] = input()

    except:
        prRed("Error while receiving data, press ENTER to try again or 'quit' for exiting")
        inp = input()
        if inp == "":
            getDbData()
        elif inp == "quit" or inp == "QUIT" or inp == "Quit":
            prRed("Exiting.....")
            sys.exit(0)
 
# Function to get user query
def getQuery():
    prCyan("Enter the SQL query : ")
    query = str(input())
    if type(query) != str:
        prRed("Fault in entered query, press ENTER to try again or 'quit' for exiting")
        inp = input()
        if inp == "":
            getQuery()
        elif inp == "quit" or inp == "QUIT" or inp == "Quit":
            prRed("Exiting.....")
            sys.exit(0)
    else:
        return query

# Function to execute user query 
def executeQuery(query,cursor):
    try:
        prGreen("Executing query......")
        output = cursor.execute(query)
        prGreen("Successfully executed query......")
        return output
    except psycopg2.InterfaceError as exc:
        prRed("Unable to execute query")
        prRed (exc.message)

# Function to connect to the database
def connect():
    prGreen("Attempting to connect to the database....")
    try:
        # Open connection to database 
        conn = psycopg2.connect(
                        host = config['host'],
                        port = config['port'],
                        database = config['database'], 
                        user = config['user'], 
                        password = config['password'])

        conn.set_session(autocommit=True)
        # Defining a Cursor
        cursor = conn.cursor()
        prGreen("Connected to database")
        prGreen("Executing Query")
        print(executeQuery(getQuery(),cursor))
    except psycopg2.InterfaceError as exc:
        prRed("Unable to connect to database")
        prRed (exc.message)
        conn = psycopg2.connect(
                        host = config['host'],
                        port = config['port'],
                        database = config['database'], 
                        user = config['user'], 
                        password = config['password'])
        cursor = conn.cursor()   

# Driver function
def main():
    getDbData()
    connect()

main()