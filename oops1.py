# initiate a class
class Employee:
    # constructor or magic method
    def __init__(self):
        print("Started Execution of Attrubutes")
        self.id = 133
        self.salary = 100000
        self.designation = "SDE"
        print("Completed Execution of Attributes")
    
    def work(self, destination):
        print("Started Execution of Methods")
        print(f"Employee is working at {destination}")


# create an object of the class
Kaushal = Employee()

# printing the attributes
# print(Kaushal.id)

# # Calling the method
# Kaushal.work("Noida")

print (type(Kaushal))


    