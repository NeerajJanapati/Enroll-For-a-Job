from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from subprocess import call
import mysql.connector



def click():
    if afname.get()=="" or alname.get()=="" or apno.get()=="" or aage.get()=="" or askill.get()=="" or acgpa.get()==""  or aemail.get()=="" or secsel.get()=="select" : 
            l=Label(apply,text="All fields are required",font=('times new roman',15),fg='red')
            l.place(x=300,y=500)

    else:
        a=afname.get()
        b=alname.get()
        c=apno.get()
        d=aage.get()
        e=askill.get()
        f=acgpa.get()
        g=secsel.get()
        h=aemail.get()
        conn= mysql.connector.connect(host="localhost",user="root",port="3307",password="1234",database="apply_db")
        my_cursor=conn.cursor()
        
        q1="insert into apply_tb(Firstname,lastname,Phonenumber,Age,skills,cgpa,companyname,email) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        v1=(a,b,c,d,e,f,g,h) 
        my_cursor.execute(q1,v1)                       
        conn.commit()
        conn.close()
        messagebox.showinfo(title="submission",message="thanks for submitting, we will send a mail to u")
















def back():
    apply.destroy()
    call(["python",'m.py'])

    
apply =Tk()
apply.geometry("1000x1000")
apply.title("apply")
label=Label(apply,text="ENTER YOUR INFO",font=('times new roman',40,'bold'),fg='green')
label.pack()

label1=Label(apply,text="Firstname:",font=('times new roman','20'),fg='blue')
label1.place(x=240,y=150)
label2=Label(apply,text="lastname",font=('times new roman','20'),fg='blue')
label2.place(x=230,y=200)
label3=Label(apply,text="phone no:",font=('times new roman','20'),fg='blue')
label3.place(x=240,y=250)
label4=Label(apply,text="Age:",font=('times new roman','20'),fg='blue')
label4.place(x=240,y=300)
label5=Label(apply,text="skills",font=('times new roman','20'),fg='blue')
label5.place(x=240,y=350)
label6=Label(apply,text="cgpa",font=('times new roman','20'),fg='blue')
label6.place(x=240,y=400)
label8=Label(apply,text="companyname",font=('times new roman','20'),fg='blue')
label8.place(x=200,y=450)
label7=Label(apply,text="Email",font=('times new roman','20'),fg='blue')
label7.place(x=240,y=500)

afname=Entry(apply,font=('times new roman',18) )
afname.place(x=370,y=150)
alname=Entry(apply,font=('times new roman',18) )
alname.place(x=370,y=200)
apno=Entry(apply,font=('times new roman',18) )
apno.place(x=370,y=250)
aage=Entry(apply,font=('times new roman',18) )
aage.place(x=370,y=300)
askill=Entry(apply,font=('times new roman',18))
askill.place(x=370,y=350)
acgpa=Entry(apply,font=('times new roman',18) )
acgpa.place(x=370,y=400)
acmynm=Entry(apply,font=('times new roman',18) )
acmynm.place(x=370,y=450)
aemail=Entry(apply,font=('times new roman',18) )
aemail.place(x=370,y=500)
btn=Button(apply,text="<--",command=back)
btn.place(x=0,y=0)

secsel=ttk.Combobox(apply,font=('times new roman',18),state="readonly")
secsel["values"]=("select","tcs","zoho","adobe","wipro")
secsel.place(x=370,y=450,height=32,width=260)
secsel.current(0)

regbtn=Button(apply,text="submit",font=('times new roman',30,'bold'),fg='green',command=click)
regbtn.place(x=370,y=550,relwidth=0.20,relheight=0.1)




apply.mainloop()