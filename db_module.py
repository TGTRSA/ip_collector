import sqlite3 as sq
import os
from typing import List

class DatabaseMaker:
    def __init__(self, databasename):
        #self.databasename = str(f"{databasename}.db"
        self.databasename = databasename + ".db"
        print(str(self.databasename))
        
    def print_db(self):
       return str(self.databasename)
    
    def establish_db(self):
        try:
            self.conn = sq.connect(self.databasename)
            print("Connection to database being created...")
            # returns the connection
            return self.conn
        except sq.Error as err:
            print(f"\033[91m An Error occured:{err}\033[0m")        
               
    def print_db(self):
        print(self.databasename)


    def create_table(self,table_name, *args: List[str]):
        #cursor = 
        columns = ", ".join(args)  # Join column definitions with commas
        sql_command = f"CREATE TABLE IF NOT EXISTS {table_name}({columns});"
        print("\033[94mAttempting to create table\033[0m")
        try:
            self.establish_db().cursor().execute(sql_command)          
            self.conn.commit()
            print(f"Created Table: {table_name} with\nParameters: {args} added")
            #self.end_connection()
        except sq.Error as e:
            print(f"\033[91m An Error occured:{e}\033[0m")
        except AttributeError as e:
            print(f"\033[91m An Error occured:{e}\033[0m")
        except SyntaxError as e:
            print(f"\033[91m An Error occured:{e}\033[0m")
        
    def insert_into_table(self, table_name: str, *args: str):
        cursor = self.establish_db().cursor()
        table_content = ", ".join(map(str, args))
        #print(f"{args}")
        sql_command = f"INSERT INTO {table_name} VALUES {table_content}"
        try:
            print(f"Attempting to insert {args}")
            print(f"INSERT INTO {table_name} VALUES {args}")
            cursor.execute(sql_command)
            print(f"Inserted ({args}) inserted into\ntable ({table_name}) ")
            self.conn.commit()
            self.end_connection()
        except sq.Error as e:
            print(f"\033[91m An Error occured:{e}\033[0m")

    def check_values(self, sql_command):
        #sql_command = "SELECT * FROM {table_name} WHERE {column_name}"
        cursor = self.establish_db().cursor()
        try:
            cursor.execute(sql_command)
            if cursor.fetchone():
                print("IP already in database")
        except sq.Error as e:
            print(f"\033[91m An Error occured:{e}\033[0m")
        except AttributeError as e:
            print(f"\033[91m An Error occured:{e}\033[0m")
        except SyntaxError as e:
            print(f"\033[91m An Error occured:{e}\033[0m")
        
        

    def view_contents(self, table_name1):
        #self.cursor = self.cursoronn_db()
        value = int(input("1. View one value from table\n2. Particular row with particular value\n"))
        #3table_name1 = str(input("Table name:"))
        if value == 1:
            # Code to view one value from one table
            try:
                self.cursor.execute(f"SELECT * FROM {table_name1}")
                rows = self.cursor.fetchall()
                for row in rows:
                    print(row)
            except sq.Error as e:
                print(f"An error occured: {e}")
        if value == 2:
            # Code to view all values from one table
            try:
                row = input("Row:")
                search_value = input("Search: ")
                self.cursor.execute(f"SELECT * FROM {table_name1} WHERE {row}=:n", {"n": f"{search_value}"})
                rows = self.cursor.fetchall()
                for row in rows:
                    print(row)
            except sq.Error as e:
                print(f"\033[91m An Error occured:{e}\033[0m")
        
    def end_connection(self):
        # Close our connection
        try:    
            self.conn.close()
        except AttributeError as e:
            print(f"\033[91m An Error occured:{e}\033[0m")

                
#if __name__ == "__main__":
#    db = database_maker("base")
#    content = ["name UNIQUE", "age int", "bat NOT NULL"]
#    database = db.establish_db()
#    db.create_table("students",*content)

