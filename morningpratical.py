import os

def register(self):
    no = input("Enter queue number: ")

    # Checking if the file is created or not
    if not os.path.exists("lunch.txt"):
        open("lunch.txt", "w").close()

    # Reading the file to check for duplicates
    with open("lunch.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if no == line.strip():
                print("Already registered")
                return  # Exit if already registered

    # Writing the new number to the file
    with open("lunch.txt", "a") as file:
        file.write(no + "\n")
        print("Successfully registered")
register()

    
        
    
