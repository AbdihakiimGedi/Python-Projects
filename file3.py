class caawiye:
    def register(self):
        no=input("Enter our que numer")
        file=open("dinner.txt","r")
        line=file.readlines()
        for i in line:
            if no in i:
                print("Sorry this number is already registred")
                return
        else:
            file=open("dinner.txt","a")
            file.write(no+"\n")
            file.close()
            print("Succesfully registred")

            #reading method
    def reading(self):
            file=open("dinner.txt","r")
            data=file.read()
            print(data)

    #Searchig data
    def search(self):
        user=input("Enter who you search")
        file=open("dinner.txt","r")
        for i in file:
            if user in i:
                print("Record was found")
                print(i)
                return
        else:
            print("Sorr we did not found that record")
            

result=caawiye()
result.register()
#result.reading()
#result.search()
