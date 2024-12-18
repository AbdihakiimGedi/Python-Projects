from tkinter import *
ob=Tk()
ob.geometry("900x600")
ob.title("Registartion form")
labelname=Label(ob,text="Enter your Name").place(x=60,y=40)
textbox=Entry(ob).place(x=60,y=40)
label2=Label(ob,text="Enter your phone number").place(x=110,y=70)
text2=Entry(ob).place(x=140,y=70)

ob.mainloop()
