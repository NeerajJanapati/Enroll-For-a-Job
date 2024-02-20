from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
from subprocess import call


def reg():
    login.destroy()
    call(["python","reg.py"])
    

def fp():
    call(["python","for.py"])



'''def m():
    show.destroy()
    call(["python",'m.py'])'''

def Login():
    if uname.get()=="" or pswd.get()=="":
        l=Label(login,text="All fields required",font=('times new roman',15),fg='red')
        l.place(x=300,y=250)
        
    
    else:
        conn=mysql.connector.connect(host="localhost",port="3307",user="root",password="1234",database="users_db")
        cur=conn.cursor()
        cur.execute("select * from my_database where Username=%s and Password=%s ",(
                                                                                        uname.get(),
                                                                                        pswd.get()
                                                                                    ))
        row=cur.fetchone()
        if row==None:
            l=Label(login,text="Incorrect username or password",font=('times new roman',15),fg='red')
            l.place(x=300,y=250)
        else:
            messagebox.showinfo("Success!","Loggedin sucessfully")
            login.destroy()
            call(["python",'m.py'])
            
        conn.commit()
        conn.close()
 
login=Tk()
login.geometry("890x600")
login.config(background='white')
login.title("Login")
#bg=ImageTk.PhotoImage(file=r"C:\Users\PRIYA\OneDrive\Pictures\depositphotos_285717846-stock-photo-living-room-interior-plants-wooden.jpg")
#lbl_bg=Label(login,image=bg)
#lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)
label=Label(login,text="Login",font=('times new roman','45','bold'),fg='blue',bg='#fefeff')
label.pack()
label1=Label(login,text="Username:",font=('times new roman','20'),fg='blue',bg='#fefeff')
label1.place(x=240,y=150)
label2=Label(login,text="Password:",font=('times new roman','20'),fg='blue',bg='#fefeff')
label2.place(x=240,y=200)
uname=Entry(login,font=('times new roman',18) )
uname.place(x=370,y=150) 
pswd=Entry(login,font=('times new roman',18),show="*" )
pswd.place(x=370,y=200)
button1=Button(login,text="Login",font=('times new roman',20),fg='green',command=Login,)
button1.place(x=250,y=300,relwidth=0.20,relheight=0.1)
label1=Label(login,text="OR",font=('times new roman',12),fg='blue')
label1.place(x=320,y=370)
label2=Label(login,text="If you don't have an account ",font=('times new roman',16),fg='blue')
label2.place(x=230,y=400)
button2=Button(login,text="SIGN IN",font=('times new roman',20),fg='green',command=reg)
button2.place(x=250,y=450,relwidth=0.20,relheight=0.1)
forgotpass=Button(login,text="Forgot Password",font=('times new roman',20),fg='green',command=fp)
forgotpass.place(x=550,y=300,relwidth=0.30,relheight=0.1)



login.mainloop()