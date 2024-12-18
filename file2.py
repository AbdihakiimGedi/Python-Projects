class caawiye:
    def test(self):
        no = input("Enter number: ")
    # Open the file and read lines
    file= open("test6.txt", "r")
    hubin = file.readlines()

    # Check if the number already exists
    for line in hubin:
        if no in line:
            print("Already registered.")
            

    
    file= open("test6.txt", "a")
    file.write(no + "\n")  
    print("Successfully registered.")
result=caawiye()
result.test()
