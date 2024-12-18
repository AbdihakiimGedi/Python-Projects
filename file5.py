class caawiye:
    def register(self,id,name,problem,status):
        person=id+"\t"+"\t"+name+"\t"+"\t"+problem+"\t"+"\t"+status+"\n"
        with open("caawiye2.txt","r")as file:
            line=file.readlines()
            for i in line:
                if person in i:
                    print("Sorry this data already registred")
                    return
            else:
                with open("caawiye2.txt","a")as file:
                    file.write(person)
                    file.close()
                    print("Succesfuly registred")

    #Reading
    def reading(self):
        with open("caawiye2.txt","r")as file:
            print(file.read())

        #Finding and searching
    def searching(self):
        with open("caawiye2.txt","r")as file:
            search=input("Enter who you search")
            for i in file:
                if search in i:
                    print("Record is found")
                    print(i)
                    return
            else:
                print("Sorry we did not found that record please confirm it register")
                    
                

result=caawiye()
#result.register(id=input("Enter your ID:"),name=input("Enter your Name:"),
 #               problem=input("Enter the problem of the laptp"),
  #              status=input("Enter the status"))
#result.reading()
result.searching()
