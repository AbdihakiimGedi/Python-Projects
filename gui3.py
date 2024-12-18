from tkinter import *
from tkinter import messagebox as msg
ob=Tk()
name=StringVar()
password=StringVar()
def display():
    txt="Waa ku salamay sxb"+"\t"+name.get()+" \n" +"Passwordka waa" +password.get()
    msg.showinfo("MessageBox",txt)

ob.geometry("900x600")
ob.title("Login form")
ob=Label(ob,text="Welcome to our application").place(x=290,y=50)
ob=Label(ob,text="Enter your Full name:").place(x=250,y=100)
ob=Entry(ob,textvariable=name).place(x=415,y=100)
ob=Label(ob,text="Enter our Password").place(x=250,y=130)
ob=Entry(ob,textvariable=password).place(x=415,y=130)
btn=Button(ob,text="LOGIN",command=display).place(x=405,y=180)
ob=mainloop()
