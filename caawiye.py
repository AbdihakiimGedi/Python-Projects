from tkinter import *
import  data3 as ex
from tkinter import messagebox as msg

ob=Tk()
ob.geometry("900x600")
ob.title("registration form")
label1=Label(ob,text="Welcome to application please fill the form").place(x=180,y=30)
id=StringVar()
name=StringVar()
password=StringVar()
problem=StringVar()
status=StringVar()
def register():
    
    if id.get()=="" and name.get()=="" and password.get()=="" and problem.get()==""and status.get()=="":
        msg.showerror("Warning","Pleae fill the data")

                    
      
    else:
        sql="insert into today(id,name,password,problem,status)values(%s,%s,%s,%s,%s)"
        values=id.get(),name.get(),password.get(),problem.get(),status.get()
        ex.cr.execute(sql,values)
        ex.db.commit()
        txt="Congratulation you registred succesfully"
        msg.showinfo("messagebox",txt)
         #Reading method
def reading():
    sql="SELECT * FROM today"
    ex.cr.execute(sql)
    result=ex.cr
    for i in result:
        print(i)
  

#Finding and sarchng
user=StringVar()
def searching():
    pass

         
                
            
label3=Label(ob,text="Enter id").place(x=200,y=110)
textid=Entry(ob,textvariable=id).place(x=290,y=110)

label3=Label(ob,text="Enter name").place(x=200,y=170)
textid=Entry(ob,textvariable=name).place(x=290,y=170)

label5=Label(ob,text="Enter password").place(x=180,y=210)
textid=Entry(ob,textvariable=password).place(x=300,y=210)

label6=Label(ob,text="Enter problem").place(x=180,y=250)
textpro=Entry(ob,textvariable=problem).place(x=300,y=250)

label7=Label(ob,text="Enter Status").place(x=180,y=300)
textstatus=Entry(ob,textvariable=status).place(x=300,y=300)

label8=Label(ob,text="Enter Status").place(x=180,y=300)
textserch=Entry(ob,textvariable=user).place(x=450,y=300)

btn1=Button(ob,text="Register",command=register).place(x=250,y=350)
btn2=Button(ob,text="Show Register",command=reading).place(x=350,y=350)
btn2=Button(ob,text="Searching",command=searching).place(x=450,y=350)
ob=mainloop();
