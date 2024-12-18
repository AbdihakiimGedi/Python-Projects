#Class and objects
class hello:
    def display(self):
        global age;
        age=int(input("Enter your age"))
    def result(self):
        res=2024-age
        print("Your age is ",res)
    
h=hello()
h.display()
h.result()
