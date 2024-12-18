from tkinter import *
import data2 as ex
ob=Tk()
name=StringVar()
age=StringVar()
def register():
    sql="insert into data(name,tell)values(%s,%s)"
    values=name.get(),age.get()
    ex.cr.execute(sql,values)
    ex.db.commit()
    print("You registred succesfully")
    
ob.geometry("900x600")
ob.title("Registration form")
labelt=Label(ob,text="Welcome to our application").place(x=150,y=40)
label1=Label(ob,text="Enter your  Name").place(x=190,y=80)
text1=Entry(ob,textvariable=name).place(x=350,y=80)

label2=Label(ob,text="Enter your Number ").place(x=190,y=120)
text12=Entry(ob,textvariable=age).place(x=350,y=120)
btn=Button(ob,text="Register",command=register).place(x=400,y=170)
ob=mainloop()
