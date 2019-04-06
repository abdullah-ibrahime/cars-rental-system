from tkinter import *
import random
import time;
from tkinter import StringVar
import sqlite3
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os

class StudentsProject:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1200x800+0+0")

        self.root.title("Aljazirah Rent System")
        self.fr = Frame(self.root, width=1200, height=100, bg="gray", relief=SUNKEN).pack()
        


        lbl_title = Label(self.fr, text=" Aljazeerah for rent the cars",font=('arial', 35, 'bold'),
                          fg="gray", bd=10,anchor='w').pack()
        lbl_title = Label(self.fr, text=" Rent car system",font=('arial', 25, 'bold'),
                          fg="gray", bd=10,anchor='w').pack()
        btnlogin = Button(self.fr, height=1, width=10, padx=2, pady=2, fg='black', font=('arial', 14, 'bold'),
                              text="Login Page", bd=10, command=self.Fun_win_login).pack()
        #=========================Database Students================

        self.db = sqlite3.connect("carRentSystem.db")
        self.db.row_factory = sqlite3.Row
        self.db.execute("create table if not exists  stud1(id integer primary key  autoincrement,"
                        "no integer,name text,carN text ,carM  text ,numbDay  text,price text,tot float)")
        self.db.commit()
        #========================End Database ======================

        self.win_students = Toplevel()
        self.win_students.withdraw()
        self.win_login = Toplevel()
        self.win_login.withdraw()
        self.win_catalog = Toplevel()
        self.win_catalog.withdraw()
        #=====================================Start login=========================

        self.win_login.title("  Login Page   ")
        self.win_students.title("Aljazeerah for rent the cars")
        self.win_catalog.title("The Cars Cataloge")
        width = 1200
        height = 800
        self.screen_width = self.win_login.winfo_screenwidth()  # width of the screen
        self.screen_height = self.win_login.winfo_screenheight()  # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (self.screen_width / 2) - (width / 2)
        y = (self.screen_height / 2) - (height / 2)
        self.win_login.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.win_login.resizable(0, 0)
        self.win_catalog.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.win_catalog.resizable(0, 0)
        # ==============================VARIABLES======================================
        self.USERNAME = StringVar()
        self.PASSWORD = StringVar()
        self.USERNAME.set('admin')
        # ==============================FRAMES=========================================
        Top = Frame(self.win_login, bd=2, relief=RIDGE)
        Top.pack(side=TOP, fill=X)
        Form = Frame(self.win_login, height=200)
        Form.pack(side=TOP, pady=20)

        # ==============================LABELS=========================================
        lbl_title = Label(Top, text="Aljazeerah for rent the cars", font=('arial', 15))
        lbl_title.pack(fill=X)
        lbl_username = Label(Form, text="Username:", font=('arial', 14), bd=15)
        lbl_username.grid(row=0, sticky="e")
        lbl_password = Label(Form, text="Password:", font=('arial', 14), bd=15)
        lbl_password.grid(row=1, sticky="e")
        self.lbl_text = Label(Form)
        self.lbl_text.grid(row=2, columnspan=2)

        # ==============================ENTRY WIDGETS==================================
        username = Entry(Form, textvariable=self.USERNAME, font=(14))
        username.grid(row=0, column=1)
        password = Entry(Form, textvariable=self.PASSWORD, show="*", font=(14))
        password.grid(row=1, column=1)

        # ==============================BUTTON WIDGETS=================================
        btn_login = Button(Form, text="Login", width=45, command=self.Fun_Login)
        btn_login.grid(pady=25, row=3, columnspan=2)
        # btn_login.bind('<Return>', self.Fun_Login)

        #============================begin of widgets Students=============
        self.f1 = Frame(self.win_students, width=1200, height=20, bg="gray", relief=SUNKEN)
        self.f1.grid(row=0, column=0)

        self.f2 = Frame(self.win_students, width=1200, height=100, relief=SUNKEN)
        self.f2.grid(row=2, column=0)

        self.f3 = Frame(self.win_students, width=1200, height=100, bg="gray", relief=SUNKEN)
        self.f3.grid(row=3, column=0)

        self.localtime = time.asctime(time.localtime(time.time()))
        self.lbInfo = Label(self.f1, font=('arial', 50, 'bold'), text="Rent Cars System", fg="gray",
                            bd=10,
                            anchor='w')
        self.lbInfo.grid(row=0, column=0)
        self.lbInfo = Label(self.f1, font=('arial', 14, 'bold'), text=self.localtime, fg="gray", bd=10,
                            anchor='w')
        
        #self.logo = PhotoImage(file="car.jpg")
        img = ImageTk.PhotoImage(Image.open("car2.jpg"))  # PIL solution
        #l.grid(row=0,colum=1)

        l=Label(image=img)
        
        l.pack()

        self.no = StringVar()
        self.name = StringVar()
        self.carN = StringVar()
        self.carM = StringVar()
        self.numbDay = StringVar()
        self.price = StringVar()
        self.tot = StringVar()

        # ============================================================================
        self.lbNo = Label(self.f2, font=('arial', 10, 'bold'), text="Phone Number", bd=10)
        self.lbNo.grid(row=0, column=0)
        self.EntryNo = ttk.Entry(self.f2, width=20, font=('Arial', 10), textvariable=self.no)
        self.EntryNo.grid(row=0, column=1, pady=1)
        self.EntryNo.focus()

        self.lbName = Label(self.f2, font=('arial', 10, 'bold'), text="Name", bd=10)
        self.lbName.grid(row=0, column=2)
        self.EntryName = ttk.Entry(self.f2, width=20, font=('Arial', 10), textvariable=self.name)
        self.EntryName.grid(row=0, column=3, pady=1)
        self.EntryName.focus()

        self.lbcarN = Label(self.f2, font=('arial', 10, 'bold'), text="Car Name", bd=10)
        self.lbcarN.grid(row=1, column=0)
        self.Entrycarn = ttk.Entry(self.f2, width=20, font=('Arial', 10), textvariable=self.carN)
        self.Entrycarn.grid(row=1, column=1, pady=1)
        self.Entrycarn.focus()

        self.lbcarM = Label(self.f2, font=('arial', 10, 'bold'), text="Car model", bd=10)
        self.lbcarM.grid(row=1, column=2)
        self.Entrycarm = ttk.Entry(self.f2, width=20, font=('Arial', 10), textvariable=self.carM)
        self.Entrycarm.grid(row=1, column=3, pady=1)
        self.Entrycarm.focus()

        self.lbNumberDay = Label(self.f2, font=('arial', 10, 'bold'), text="Number of days", bd=10)
        self.lbNumberDay.grid(row=2, column=0)
        self.EntryNumberDay = ttk.Entry(self.f2, width=20, font=('Arial', 10), textvariable=self.numbDay)
        self.EntryNumberDay.grid(row=2, column=1, pady=1)
        self.EntryNumberDay.focus()

        self.lbPrice = Label(self.f2, font=('arial', 10, 'bold'), text="Price for day", bd=10)
        self.lbPrice.grid(row=2, column=2)
        self.EntryPrice = ttk.Entry(self.f2, width=20, font=('Arial', 10), textvariable=self.price)
        self.EntryPrice.grid(row=2, column=3, pady=1)
        self.EntryPrice.focus()

        self.lbTot = Label(self.f2, font=('arial', 10, 'bold'), text="Total", bd=10)
        self.lbTot.grid(row=3, column=1)
        self.EntryTot = ttk.Entry(self.f2, width=20, font=('Arial', 10), textvariable=self.tot,state="readonly")
        self.EntryTot.grid(row=3, column=2, pady=1)
        self.EntryTot.focus()

        # ===============================================================================

        self.btnShow = Button(self.f2, height=1, width=10, padx=2, pady=2, fg='black', font=('arial', 10, 'bold'),
                              text="Show", bd=10, command=self.FunShow).grid(row=4, column=0)

        self.btnAdd = Button(self.f2, height=1, width=10, padx=2, pady=2, fg='black', font=('arial', 10, 'bold'),
                             text="Add", bd=10, command=self.FunAdd).grid(row=4, column=1)

        self.btnDel = Button(self.f2, height=1, width=10, padx=2, pady=2, fg='black', font=('arial', 10, 'bold'),
                             text="Delete", bd=10, command=self.FunDel).grid(row=4, column=2)

        self.btnUpdate = Button(self.f2, height=1, width=10, padx=2, pady=2, fg='black', font=('arial', 10, 'bold'),
                                text="Update", bd=10, command=self.FunUpdate).grid(row=4, column=3)
        self.btnClear = Button(self.f2, height=1, width=10, padx=2, pady=2, fg='black', font=('arial', 10, 'bold'),
                               text="Clear", bd=10, command=self.FunClear).grid(row=5, column=1)
        btn_back = Button(self.f2, height=1, width=10, padx=2, pady=2, fg='black', font=('arial', 10, 'bold'),
                          text="Back", bd=10, command=self.Back).grid(row=5, column=2)
        btn_catalog = Button(self.f2, height=1, width=10, padx=2, pady=2, fg='black', font=('arial', 10, 'bold'),
                          text="Cars Catalog", bd=10,command=self.CatalogeWind).grid(row=5, column=3)
        # ============================================================================
        self.lableCata=Label(self.win_catalog,font=('arial', 20, 'bold'), text="The Cars Cataloge", bd=10)
        self.lableCata.grid( column=2,row=0)
        self.btn_back = Button(self.win_catalog, height=1, width=10, padx=2, pady=2, fg='black', font=('arial', 10, 'bold'),
                          text="Back", bd=10, command=self.Back2).grid(row=4, column=0)
        
        self.ford = ImageTk.PhotoImage(Image.open("ford.jpg"))  # PIL solution
        self.l=Label(self.win_catalog,image=self.ford)
        self.l.grid(column=1,row=2)

        self.datsun = ImageTk.PhotoImage(Image.open("datsun.jpg"))  # PIL 
        self.l=Label(self.win_catalog,image=self.datsun)
        self.l.grid(column=2,row=2)

        
        self.patrol = ImageTk.PhotoImage(Image.open("patrol.jpg"))  # PIL solution
        self.l=Label(self.win_catalog,image=self.patrol)
        self.l.grid(column=3,row=2)
        
        self.jmc = ImageTk.PhotoImage(Image.open("jmc.jpg"))  # PIL solution
        self.l=Label(self.win_catalog,image=self.jmc)
        self.l.grid(column=1,row=5)

        
        self.mazda3 = ImageTk.PhotoImage(Image.open("mazda3.jpg"))  # PIL solution
        self.l=Label(self.win_catalog,image=self.mazda3)
        self.l.grid(column=2,row=5)

        
        self.corola = ImageTk.PhotoImage(Image.open("corola.jpg"))  # PIL 
        self.l=Label(self.win_catalog,image=self.corola)
        self.l.grid(column=3,row=5)




        self.lableford=Label(self.win_catalog,font=('arial', 10, 'bold'), text="Ford 2007", bd=10)
        self.lableford.grid( column=1,row=3)
        
        self.labledatsun=Label(self.win_catalog,font=('arial', 10, 'bold'), text="Datsun 2015", bd=10)
        self.labledatsun.grid( column=2,row=3)

        self.lablepatrol=Label(self.win_catalog,font=('arial', 10, 'bold'), text="Patrol 2008", bd=10)
        self.lablepatrol.grid( column=3,row=3)

        self.lableJMC=Label(self.win_catalog,font=('arial', 10, 'bold'), text="JMC 2017", bd=10)
        self.lableJMC.grid( column=1,row=6)

        self.lableMazda3=Label(self.win_catalog,font=('arial', 10, 'bold'), text="Ford 2018", bd=10)
        self.lableMazda3.grid( column=2,row=6)

        self.lableCorola=Label(self.win_catalog,font=('arial', 10, 'bold'), text="Ford 2011", bd=10)
        self.lableCorola.grid( column=3,row=6)


        
        



        
        # ============================================================================

        self.tv = ttk.Treeview(self.f3)
        self.tv.grid(row=0, column=0)

        self.tv.heading('#0', text='ID')

        self.tv.configure(column=('#Phone', '#Name', '#CarName', '#CarModel', '#NumberOfDays', '#PriceForDay', '#Total'))
        self.tv.column('#0', width=80, anchor='center')
        self.tv.column('#Phone', width=80, anchor='center')
        self.tv.column('#Name', width=80, anchor='center')
        self.tv.column('#CarName', width=80, anchor='center')
        self.tv.column('#CarModel', width=80, anchor='center')
        self.tv.column('#NumberOfDays', width=80, anchor='center')
        self.tv.column('#PriceForDay', width=80, anchor='center')
        self.tv.column('#Total', width=80, anchor='center')

        self.tv.heading('#Phone', text='Phone')
        self.tv.heading('#Name', text='Name')
        self.tv.heading('#CarName', text='Car Name')
        self.tv.heading('#CarModel', text='Car Model')
        self.tv.heading('#NumberOfDays', text='Number Of Days')
        self.tv.heading('#PriceForDay', text='Price For Day')
        self.tv.heading('#Total', text='Total')

        # self.tv.bind("<<TreeviewSelect>>", self.on_tree_select2)
        self.binding()

    #======================End widgets Students=========================
        self.root.mainloop()
    #======================begin of login Funcations ===================

    def Fun_win_login(self):
        print("your are login")
        self.root.withdraw()
        #self.root.resizable(0,0)
        self.win_login.deiconify()

    def Fun_Login(self, event=None):
        self.Database()
        if self.USERNAME.get() == "" or self.PASSWORD.get() == "":
            self.lbl_text.config(text="Please complete the required field!", fg="red")
        else:
            cursor.execute("SELECT * FROM `users` WHERE `username` = ? AND `password` = ?",
                           (self.USERNAME.get(), self.PASSWORD.get()))
            if cursor.fetchone() is not None:
                self.HomeWindow()
                self.USERNAME.set("")
                self.PASSWORD.set("")
                self.lbl_text.config(text="")
            else:
                self.lbl_text.config(text="Invalid username or password", fg="red")
                self.USERNAME.set("")
                self.PASSWORD.set("")
        cursor.close()
        conn.close()
        # ==============================METHODS========================================

    def Database(self):
        global conn, cursor
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `users` (user_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
        cursor.execute("SELECT * FROM `users` WHERE `username` = 'admin' AND `password` = 'admin'")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO `users` (username, password) VALUES('admin', 'admin')")
            conn.commit()

    def HomeWindow(self):
        messagebox.showinfo(title="Login!", message="Successfully Login!")
        self.page2()

        width = 1200
        height = 800
        x = (self.screen_width / 2) - (width / 2)
        y = (self.screen_height / 2) - (height / 2)

        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.resizable(0, 0)
    def page2(self):
        # seems to just remove the window from the screen, after which the window has a state of "withdrawn"
        self.win_login.withdraw()
        self.win_students.deiconify()

    def Back(self):
        self.win_students.withdraw()
        self.root.deiconify()
        self.root.resizable(0, 0)

    def Back2(self):
        self.win_catalog.withdraw()
        self.win_students.deiconify()
        self.win_students.resizable(0, 0)
        
    def CatalogeWind(self):
        self.page3()

        width = 1200
        height = 800
        x = 0
        y = 0

        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.resizable(0, 0)
    def page3(self):
        # seems to just remove the window from the screen, after which the window has a state of "withdrawn"
        self.win_students.withdraw()
        self.win_catalog.deiconify()   

    def binding(self):
        self.tv.bind("<<TreeviewSelect>>", self.on_tree_select2)
    # ===============================================================================
    def on_tree_select(self, event):
        print("selected items:")
        for item in self.tv.selection():
            item_text = self.tv.item(item, "text")
            print(item_text)
            self.selected_item = item_text
        return item_text
          

    def FunAdd(self):
        no = self.EntryNo.get()
        name = self.EntryName.get()
        carN = self.Entrycarn.get()
        carM = self.Entrycarm.get()
        numbDay = self.EntryNumberDay.get()
        price = self.EntryPrice.get()
        tot=int(price)*int(numbDay)
        if (self.EntryNo.get()=="" or self.EntryName.get()=="" or self.Entrycarn.get() == "" or self.Entrycarm.get() == "" or self.EntryNumberDay.get() == "" or self.EntryPrice.get() == ""):
            messagebox.showinfo(title="Add info", message='Please Insert Data !!!!!')
        else:
            self.db.execute("insert into stud1(no,name,carN,carM,numbDay,price,tot) values (?, ? , ? , ? , ?, ? , ?)",
                            (no,name,carN,carM,numbDay,price,tot))
            self.db.commit()
            messagebox.showinfo(title="Add info", message='added')
            self.FunShow()
            self.FunClear()
    # ==================tree.delete(*tree.get_children())=============================================================

    def FunClear(self):
        self.EntryName.delete(0, 'end')
        self.EntryNo.delete(0, 'end')
        self.Entrycarn.delete(0, 'end')
        self.Entrycarm.delete(0, 'end')
        self.EntryNumberDay.delete(0, 'end')
        self.EntryPrice.delete(0, 'end')
        self.EntryTot.delete(0,'end')
         

    def FunShow(self):
        # x = self.tv.get_children()        for item in x:            self.tv.delete(item)

        self.tv.delete(*self.tv.get_children())

        
        cursor = self.db.execute("select * from stud1")
        for row in cursor:
            self.tv.insert('', 'end', '{}'.format(row['id']), text=row['id'])
            self.tv.set('{}'.format(row['id']), '#Phone', row['no']) 
            self.tv.set('{}'.format(row['id']), '#Name', row['name'])
            self.tv.set('{}'.format(row['id']), '#CarName', row['carN'])
            self.tv.set('{}'.format(row['id']), '#CarModel', row['carM'])
            self.tv.set('{}'.format(row['id']), '#NumberOfDays', row['numbDay'])
            self.tv.set('{}'.format(row['id']), '#PriceForDay', row['price'])
            self.tv.set('{}'.format(row['id']), '#Total', row['tot'])

        item_count = len(self.tv.get_children())
        

      # ===============================================================================
    def on_tree_select2(self, event):

        selected_item = self.tv.selection()[0]
        cursor = self.db.execute("select * from stud1 where id=?", (selected_item,))

        for row in cursor:
            self.no.set(str(row['no']))
            self.name.set(str(row['name']))
            self.carN.set(str(row['carN']))
            self.carM.set(str(row['carM']))
            self.numbDay.set(str(row['numbDay']))
            self.price.set(str(row['price']))
            self.tot.set(str(row['tot']))

        # ======================================================

    def FunUpdate(self):

        selected_item = self.tv.selection()[0]
        if (self.EntryNo.get()=="" or self.EntryName.get()=="" or self.Entrycarn.get() == "" or self.Entrycarm.get() == "" or self.EntryNumberDay.get() == "" or self.EntryPrice.get() == ""):
            messagebox.showinfo(title="Add info", message='Please Insert Data !!!!!')
        else:
            '''self.EntryName.delete(0, 'end')
            self.EntryNo.delete(0, 'end')
            self.Entrycarn.delete(0, 'end')
            self.Entrycarm.delete(0, 'end')
            self.EntryDateRent.delete(0, 'end')
            self.EntryDateReturn.delete(0, 'end')
            self.EntryTot.delete(0,'end')'''
           
            no = self.EntryNo.get()
            name = self.EntryName.get()
            carN = self.Entrycarn.get()
            carM = self.Entrycarm.get()
            numbDay= self.EntryNumberDay.get()
            price = self.EntryPrice.get()
            tot = int(price)*int(numbDay)





            

            id=selected_item
            print("id=====", selected_item)

            self.db.execute('Update stud1 set no=? ,name=?, carN=?, carM=?, numbDay=? ,price=?,tot=?   where id=?'
                            , (no,name,carN,carM,numbDay,price,tot, id))
            self.db.commit()
            messagebox.showinfo(title="Add info", message='Data is Updated')
            self.FunShow()
            self.FunClear()

    # ===============================================================================

    def FunDel(self):
        
        conn = sqlite3.connect("carRent.db")
        self.db.row_factory = sqlite3.Row
        selected_item = self.tv.selection()[0]
        print('selected_item', selected_item)  # it prints the selected row id
        cur = conn.cursor()
        cur.execute("DELETE FROM stud1 WHERE id=?", (selected_item,))
        conn.commit()

        self.tv.delete(selected_item)
        messagebox.showinfo(title="Add info", message='Record is deleted')
        self.FunShow()
        self.FunClear()
        
    # =========================================

    def delete(self):

         id=self.tv.bind("<<TreeviewSelect>>", self.on_tree_select)
         self.db.execute("DELETE FROM stud1 where id=?", (id))
         self.db.commit
         print(" DEL id=====",self.selected_item)
         self.FunShow()
         messagebox.showinfo(title="Add info", message='Record is deleted')

    def remove_item(self):
        selected_item = self.treeview.selection()[0]
        self.treeview.delete(selected_item)
        print("id=====", id)


    def update(self):

        id= selected_item = self.tv.selection()[0]
        self.db.execute('Update stud set no=? ,name=?, carN=?, carM=?, numbDay=?,price=?,tot=? where id==?' , (selected_item,))
        self.db.commit
        # self.FunShow()
        print("id=====", selected_item)
        messagebox.showinfo(title="Add info", message='Record is deleted')
        self.db.commit()
        self.FunShow()


def main():
    StudentsProject()

#==============================INITIALIATION==================================
if __name__ == '__main__':
    main()
