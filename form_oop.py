from tkinter import *
from tkinter import ttk
from form_db import formDB
import random
import string

class form(formDB):
    def __init__(self):
        super().__init__()

        self.win = Tk()
        self.win.geometry('500x730')
        self.win.title("Interviewer's Form")
        self.win.resizable(0,0)
        try:self.win.wm_iconbitmap("icon.ico")
        except:pass

        self.labels = ['id','Last Name *','First Name *','Gender','Email *','Role','Address 1 *','Address 2','City','Region Code','Phone Home *','Phone Work']
        self.forInsert()

    
    def forInsert(self):
        self.e = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.ulabel = Label(self.win,text="FORM",font=('calibri',20),fg='black').pack(side=TOP,anchor=N)

        for lbl in range(13):
                lbl = Label(self.win,text=self.labels[lbl-1],font=('italic',10),fg='black').place(x=20,y=lbl*50)
        try:
# ==============creating entries
            for lbl in range(1, 4):
                self.e[lbl]= Entry(self.win,font=('calibri',10),fg='black', width=40)
                self.e[lbl].place(x=150,y=lbl*50)
            for lbl in range(5,6):
                self.e[lbl]= Entry(self.win,font=('calibri',10),fg='black', width=40)
                self.e[lbl].place(x=150,y=lbl*50)
            for lbl in range(7,10):
                self.e[lbl]= Entry(self.win,font=('calibri',10),fg='black', width=40)
                self.e[lbl].place(x=150,y=lbl*50)
            for lbl in range(11,13):
                self.e[lbl]= Entry(self.win,font=('calibri',10),fg='black', width=40)
                self.e[lbl].place(x=150,y=lbl*50)

# ==============creating drop down
            for lbl in range(4,5):
                self.e[lbl]= ttk.Combobox(self.win, width=43, values=["Male", "Female"])
                self.e[lbl].place(x=150,y=lbl*50)
            for lbl in range(6,7):
                self.e[lbl]= ttk.Combobox(self.win, width=43, values=["Head", "Tail"])
                self.e[lbl].place(x=150,y=lbl*50)
            for lbl in range(10,11):
                self.e[lbl]= ttk.Combobox(self.win, width=43, values=["NC", "NE", "NW", "SE", "SS", "SW"])
                self.e[lbl].place(x=150,y=lbl*50)

        except: pass

        self.submit = Button(self.win,text='submit',width=20,bg='black', borderwidth=5,command=self.insert,fg='grey')
        self.submit.pack(side=BOTTOM, fill=X)

        self.win.mainloop()


if __name__== "__main__":
    
    form()
