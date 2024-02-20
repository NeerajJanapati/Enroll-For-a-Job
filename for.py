from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
from subprocess import call



Forpass=Tk()
Forpass.geometry("500x600")
Forpass.title("Forgot Password")
#bg=ImageTk.PhotoImage(file=r"C:\Users\nikhi\OneDrive\Pictures\forpas img.jpg")
#lbl_bg=Label(Forpass,image=bg)
#lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)
label=Label(Forpass,text="Forgot Password",font=('times new roman',35,'bold'),fg='brown')
label.pack()
label2= Label(Forpass,text="Select the question :",font=('times new roman',20,'bold'),fg='brown')
label2.place(x=30,y=130)
label3= Label(Forpass,text="Answer the question :",font=('times new roman',20,'bold'),fg='brown')
label3.place(x=30,y=230)
label4= Label(Forpass,text="Enter the new password :",font=('times new roman',20,'bold'),fg='brown')
label4.place(x=30,y=330)
sel=ttk.Combobox(Forpass,font=('times new roman',20),state='readonly')
sel["values"]=("select","Your birth place?","Your first school?","Your favorite food?")
sel.place(x=30,y=180,height=32,width=260)
sel.current(0)
box1=Entry(Forpass,font=('times new roman',20))
box1.place(x=30,y=280)
box2=Entry(Forpass,font=('times new roman',20))
box2.place(x=30,y=380)
btn=Button(Forpass,text="Reset password",font=('times new roman',30,'bold'),fg='brown')
btn.place(x=120,y=450,height=60,width=270)

Forpass.mainloop()