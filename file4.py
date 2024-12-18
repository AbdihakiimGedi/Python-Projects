#Project about file
class information:
    def person(self):
        fullname=input("Enter your full name")
        gender=input("Enter your gender")
        birthdate=input("Enter your birth date")
        status=input("Enter your martial status")
        number=input("Enter your phone number")
        school=input("Enter your school name")
        average=(input("Enter your grade average"))
        responsible=input("Who responsible your fee payment")
        all=fullname+"\t"+"\t"+gender+"\t"+"\t"+birthdate+"\t"+"\t"+status+"\t"+"\t"+number+"\t"+"\t"+school+"\t"+"\t"+average+"\t"+"\t"+responsible+"\n"
        with open("university.txt","r")as file:
            line=file.readlines()
        for i in line:
            if all in i:
                print("Sorry this data is already registred")
                return
        else:
            with open("university.txt","a")as file:
                file.write(all+"\n")
                print("Register succesfully")
                #Reading data from the file
    def reading(self):
              with open("university.txt","r")as file:
                  data=file.read()
                  print(data)
                  #Searching data in the file
    def search(self):
              with open("university.txt","r")as file:
                  user=input("Enter who you search").strip()
                  for i in file:
                      if user in i.strip(): 
                          print("Record was found")
                          print(i)
                          return
                  else:
                    print("Sorry we did not found that data lease confirm it you register or not")
#object of the class                    
register=information()
#register.person()
#register.reading()
register.search()
