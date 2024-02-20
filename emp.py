from tkinter import*
from tkinter import ttk
from subprocess import call
def back():
    emp.destroy()
    call(["python",'m.py'])
emp= Tk()
emp.geometry("600x600")
notebook=ttk.Notebook(emp)

tab1= Frame(notebook)
tab2= Frame(notebook)
tab3= Frame(notebook)
tab4= Frame(notebook)

notebook.add(tab1,text="emp 1 tcs")
notebook.add(tab2,text="emp 2 zoho")
notebook.add(tab3,text="emp 3 adobe")
notebook.add(tab4,text="emp  4 wipro")


notebook.pack(expand=True,fill="both")

Label(tab1,text="1.the employee details of tcs  employee name: ratan tata  ").pack()
Label(tab1,text="phone number : 9394959697 ").pack()
Label(tab2,text="2.the employee details of zoho employee name: prakesh ").pack()
Label(tab2,text="phone number : 9323457823  ").pack()
Label(tab3,text="3.the employee details of adobe  employee name: charan reddy ").pack()
Label(tab3,text="phone number : 9434567834 ").pack()
Label(tab4,text="4, the employee details of wipro  employee name: azimprem ").pack()
Label(tab4,text="phone number : 9394959697 ").pack()
btn=Button(emp,text="<--",command=back)
btn.place(x=300,y=400)
emp.mainloop()