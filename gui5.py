from tkinter import *
import data1 as exe
ob=Tk()
ob.geometry("900x600")
name=StringVar()
password=StringVar()
addres=StringVar()
def register():
    #all=name.get()+" "+password.get()
    sql="insert into persons(name,tell)values(%s,%s)"
    values=name.get(),password.get()
    exe.cr.execute(sql,values)
    exe.db.commit()
    print("Succesfully registred")
    
    
label1=Label(ob,text="Enter your name").place(x=120,y=50)
text1=Entry(ob,textvariable=name).place(x=250,y=50)
label2=Label(ob,text="Enter your name").place(x=120,y=90)
 

text2=Entry(ob,textvariable=password).place(x=250,y=90)

label3=Label(ob,text="Enter your addres").place(x=120,y=190)
text3=Entry(ob,textvariable=addres).place(x=290,y=190)
btn=Button(ob,text="Register Now",command=register).place(x=190,y=140)
ob=mainloop()
