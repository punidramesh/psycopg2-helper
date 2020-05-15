#!/usr/bin/python3

import psycopg2
import sys

config = {}

def getDbData():
    try : 
        
        print("Enter host name or press ENTER for localhost : ")
        config['host'] = input()
        if config['host'] == "": config['host'] = "localhost"
        print("Enter port number or press ENTER for using port '5432' : ")
        config['port'] = input()
        if config['port'] == "": config['port'] = "5432"
        print("Enter database name : ")
        config['database'] = input()
        print("Enter user name : ")
        config['user'] = input()
        print("Enter password : ")
        config['password'] = input()

    except:
        print("Error while receiving data, press ENTER to try again or 'quit' for exiting")
        inp = input()
        if inp == "":
            getDbData()
        elif inp == "quit" or inp == "QUIT" or inp == "Quit":
            print("Exiting.....")
            sys.exit(0)

def getQuery():
    print("Enter the SQL query : ")
    query = str(input())
    if isinstance(query, str):
        print("Fault in entered query, press ENTER to try again or 'quit' for exiting")
        inp = input()
        if inp == "":
            getQuery()
        elif inp == "quit" or inp == "QUIT" or inp == "Quit":
            print("Exiting.....")
            sys.exit(0)

def executeQuery(query,conn):
    try:
        output = conn.execute(query)
        print("Successfully executed query")
        return output
    except psycopg2.InterfaceError as exc:
        print("Unable to connect to database")
        print (exc.message)


def connect():
    print("Attempting to connect to the database....")
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
        print("Connected to database")
        print("Executing Query")
        executeQuery(getQuery())
    except psycopg2.InterfaceError as exc:
        print("Unable to connect to database")
        print (exc.message)
        conn = psycopg2.connect(
                        host = config['host'],
                        port = config['port'],
                        database = config['database'], 
                        user = config['user'], 
                        password = config['password'])
        cursor = conn.cursor()   

def main():
    getDbData()
    getQuery()
    connect()
    executeQuery() 

main()