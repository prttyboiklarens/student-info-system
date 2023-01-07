from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3


def Database():
    global conn, cursor
   
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
   
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS REGISTRATION (RID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FNAME TEXT, LNAME TEXT, GENDER TEXT, ADDRESS TEXT, CONTACT TEXT)")


def DisplayForm():
   
    display_screen = Tk()
   
    display_screen.geometry("1200x500")
    
    display_screen.title("SIS")
    global tree
    global SEARCH
    global fname,lname,gender,address,contact
    SEARCH = StringVar()
    fname = StringVar()
    lname = StringVar()
    gender = StringVar()
    address = StringVar()
    contact = StringVar()
  
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
   
    LFrom = Frame(display_screen, width="350",bg="#F0FFFF")
    LFrom.pack(side=LEFT, fill=Y)
    
    LeftViewForm = Frame(display_screen, width=500,bg="#F0FFFF")
    LeftViewForm.pack(side=LEFT, fill=Y)
   
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)
   
    lbl_text = Label(TopViewForm, text="STUDENT INFORMATION SYSTEM", font=("verdana", 25), width=600,bg="yellow")
    lbl_text.pack(fill=X)
   
    Label(LFrom, text="First Name  ", font=("Arial", 12),bg="#F0FFFF",fg="black").pack(side=TOP)
    Entry(LFrom,font=("Arial",10,"bold"),textvariable=fname).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Last Name ", font=("Arial", 12),bg="#F0FFFF",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=lname).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Gender ", font=("Arial", 12),bg="#F0FFFF",fg="black").pack(side=TOP)
    
    gender.set("Select Gender")
    content={'Male','Female'}
    OptionMenu(LFrom,gender,*content).pack(side=TOP, padx=10, fill=X)


    Label(LFrom, text="Address ", font=("Arial", 12),bg="#F0FFFF",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=address).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Contact ", font=("Arial", 12),bg="#F0FFFF",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=contact).pack(side=TOP, padx=10, fill=X)
    Button(LFrom,text="Submit",font=("Arial", 10, "bold"),command=register,bg="#FFD700",fg="white").pack(side=TOP, padx=10,pady=5, fill=X)

   
    lbl_txtsearch = Label(LeftViewForm, text="Enter Fname to Search", font=('verdana', 10),bg="#F0FFFF")
    lbl_txtsearch.pack()
   
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
   
    btn_search = Button(LeftViewForm, text="Search", command=SearchRecord,bg="yellow")
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
   
    btn_view = Button(LeftViewForm, text="View All", command=DisplayData,bg="yellow")
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset,bg="yellow")
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
   
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete,bg="yellow")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    
    btn_delete = Button(LeftViewForm, text="Update", command=Update,bg="yellow")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
   
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("Student Number", "Name", "Lastname", "Email","Address","Contact"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    
    tree.heading('Student Number', text="STUDENT NUMBER", anchor=W)
    tree.heading('Name', text="FIRSTNAME", anchor=W)
    tree.heading('Lastname', text="LASTNAME", anchor=W)
    tree.heading('Email', text="GENDER", anchor=W)
    tree.heading('Address', text="ADDRESS", anchor=W)
    tree.heading('Contact', text="CONTACT", anchor=W)
    
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=130)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()

def Update():
    Database()
   
    fname1=fname.get()
    lname1=lname.get()
    gender1=gender.get()
    address1=address.get()
    contact1=contact.get()
    
    if fname1=='' or lname1==''or gender1=='' or address1==''or contact1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        
        conn.execute('UPDATE REGISTRATION SET FNAME=?,LNAME=?,GENDER=?,ADDRESS=?,CONTACT=? WHERE RID = ?',(fname1,lname1,gender1,address1,contact1, selecteditem[0]))
        conn.commit()
        tkMessageBox.showinfo("Message","Updated successfully")
        
        Reset()
        
        DisplayData()
        conn.close()

def register():
    Database()
    
    fname1=fname.get()
    lname1=lname.get()
    gender1=gender.get()
    address1=address.get()
    contact1=contact.get()
   
    if fname1=='' or lname1==''or gender1=='' or address1==''or contact1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
       
        conn.execute('INSERT INTO REGISTRATION (FNAME,LNAME,GENDER,ADDRESS,CONTACT) \
              VALUES (?,?,?,?,?)',(fname1,lname1,gender1,address1,contact1));
        conn.commit()
        tkMessageBox.showinfo("Message","Stored successfully")
       
        DisplayData()
        conn.close()
def Reset():
    
    tree.delete(*tree.get_children())
    
    DisplayData()
   
    SEARCH.set("")
    fname.set("")
    lname.set("")
    gender.set("")
    address.set("")
    contact.set("")
def Delete():
   
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM REGISTRATION WHERE RID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


def SearchRecord():
    
    Database()
    
    if SEARCH.get() != "":
        
        tree.delete(*tree.get_children())
        
        cursor=conn.execute("SELECT * FROM REGISTRATION WHERE FNAME LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        
        fetch = cursor.fetchall()
        
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def DisplayData():
   
    Database()
    
    tree.delete(*tree.get_children())
    
    cursor=conn.execute("SELECT * FROM REGISTRATION")
   
    fetch = cursor.fetchall()
    
    for data in fetch:
        tree.insert('', 'end', values=(data))
        tree.bind("<Double-1>",OnDoubleClick)
    cursor.close()
    conn.close()
def OnDoubleClick(self):
    
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
   
    fname.set(selecteditem[1])
    lname.set(selecteditem[2])
    gender.set(selecteditem[3])
    address.set(selecteditem[4])
    contact.set(selecteditem[5])


DisplayForm()
if __name__=='__main__':
    
    mainloop()