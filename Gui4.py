from tkinter import *
ob=Tk()
ob.geometry("900x600")
name=StringVar()
email=StringVar()
password=StringVar()
confirm=StringVar()
user=StringVar()
def register():
    all=name.get()+"\t"+"\t"+email.get()+"\t"+"\t"+password.get()+"\t"+"\t"+confirm.get()+"\n"+"\n".strip()
    file=open("test14.txt","r")
    line=file.readlines()
    for i in line:
        if all in i:
            print("Sorry this data already registred")
            return
    else:
        file=open("test14.txt","a")
        file.write(all)
        file.close()
        result=Label(ob,text="Registred succesfully").place(x=350,y=308)
        
           
       #Reading method
def reading():
      file=open("test14.txt","r")
      data=file.read()
      read=Label(ob,text=data).place(x=110,y=305)
      #Searching method
def searching():
    file=open("test14.txt","r")
    #search=user.get()
    if user.get()== " ":
        print("Please enter value")
    else:
        for i in file:
            if user.get() in i.strip():
                find=Label(ob,text="Record is founded"+"\n"+i).place(x=195,y=380)
                return
            else:
                notfind=Label(ob,text="Record is not founded please confirm to registrered that record").place(x=195,y=380)
          
   
ob.geometry("900x1024")
ob.title("Registration form")
ob=Label(ob,text="Welcome to our application please fill the form").place(x=150,y=40)
label1=Label(ob,text="Enter your full name").place(x=210,y=80)
text1=Entry(ob,textvariable=name).place(x=370,y=80)


label2=Label(ob,text="Enter your Email").place(x=210,y=125)
text2=Entry(ob,textvariable=email).place(x=370,y=125)

label3=Label(ob,text="create new  password").place(x=210,y=175)
text3=Entry(ob,textvariable=password).place(x=370,y=170)

label4=Label(ob,text="confirm   password").place(x=200,y=215)
text4=Entry(ob,textvariable=confirm).place(x=370,y=215)

btn=Button(ob,text="Register",command=register).place(x=210,y=280)

btn=Button(ob,text="Show registerations ",command=reading).place(x=310,y=280)
btn=Button(ob,text="Search ",command=searching).place(x=420,y=370)
searchtext=Entry(ob,textvariable=user).place(x=210,y=370)


ob=mainloop()
