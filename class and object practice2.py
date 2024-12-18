class person:
    def information(self):
        global name
        name=input("Enter your name")
        global tell
        tell=input("Enter phone number")
        global address
        address=input("Enter your address")
        global status
        status=input("Enter your status")
    def display(self):
        print("My name is :",name)
        print("Pone Number:",tell)
        print("My address is: ",address)
        print("M status is :",status)


