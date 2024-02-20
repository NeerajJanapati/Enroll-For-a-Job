from tkinter import*
from subprocess import call
from tkinter import font
def ap():
    show.destroy()
    call(["python",'ap.py'])
def apti():
    show.destroy()
    call(["python",'apti.py'])
def emp():
    show.destroy()
    call(["python",'emp.py'])


show =Tk()
show.geometry("700x600")
show.title("DETAILS")
listbox1= Listbox(show,width=30)
listbox1.pack(side=LEFT)

listbox1.insert(1,"TCS")
listbox1.insert(2,"")
listbox1.insert(2,"HIRING FOR FRESHERS")
listbox1.insert(3,"for software testing")
listbox1.insert(4,"")
listbox1.insert(5,"cgpa should be above 80%")

submit_button=Button(show,text=" apply",command=ap)
submit_button.place(x=300,y=300)


submit_button=Button(show,text="apti Q",command=apti)
submit_button.place(x=350,y=300)


submit_button=Button(show,text="deltails",command=emp)
submit_button.place(x=400,y=300)

listbox2= Listbox(show,width=30)
listbox2.pack(side=RIGHT)
listbox2.insert(1,"zoho")
listbox2.insert(2,"")
listbox2.insert(2,"HIRING FOR FRESHERS")
listbox2.insert(3," looking for software developer")
listbox2.insert(4,"")
listbox2.insert(5,"cgpa should be above 80%")




listbox3= Listbox(show,width=35)
listbox3.pack(side=BOTTOM)
listbox3.insert(1,"adobe")
listbox3.insert(2,"")
listbox3.insert(2,"HIRING FOR EXPERIENCE CANDIDATE")
listbox3.insert(3,"looking for team leader")
listbox3.insert(4,"")
listbox3.insert(5,"cgpa should be above 80%")




listbox4= Listbox(show,width=30)
listbox4.pack()

listbox4.insert(1,"wipro")
listbox4.insert(2,"")
listbox4.insert(2,"HIRING FOR FRESHERS")
listbox4.insert(3,"looking for backend developer")
listbox4.insert(4,"")
listbox4.insert(5,"cgpa should be above 80%")




show.mainloop()
