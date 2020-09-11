from tkinter import *
import tkinter.messagebox as msg
import mysql.connector as mysql


class formDB():

        def __init__(self):
                try:
                        self.connection = mysql.connect(host='localhost',password="your_password",user='root', database='database_name') # use your db_name and your db_password
                except:
                        msg.showwarning("You are not connected to server(localhost)")
                else:
                        self.cur = self.connection.cursor()
                        db= """CREATE TABLE IF NOT EXISTS new_interview (id varchar(15), L_name varchar(250), F_name varchar(250), Gender varchar(250), Email varchar(250), Role varchar(100), Address_1 varchar(250), Address_2 varchar(250), City varchar(250), Region_Code varchar(250), Phone_Home int(15), Phone_Work int(15));"""
                        self.cur.execute(db)

        def insert(self):
                try:
                        self.val = []
                        for i in range(1,13):
                                self.val.append(self.e[i].get())
                        self.val[0]= self.val[0].upper()
                        if (self.val[1]=="" or self.val[2]=="" or self.val[4]=="" or self.val[6]=="" or self.val[10]==""):
                                msg.showerror("Compulsory", "fields with * are compulsory")
                        else:
                                self.query="""INSERT INTO new_interview (id, L_name, F_name, Gender, Email, Role,Address_1, Address_2, City, Region_Code, Phone_Home, Phone_Work)
                                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                                self.cur.execute(self.query,self.val)
                                self.connection.commit();
                                self.cur.close()
                                for i in range(1, 13):
                                        self.e[i].delete(0, 'end')

                                msg.showinfo("inserted Successfully.")

                except Exception as ex:
                        print(ex,'\n error in inserting values')

        
if __name__=="__main__":
        app = formDB()