class Employee:
    
    def __init__(self):
        print("Employee Credited")
    def __del__(self):
        print("Destructor Called")

def create_obj():
    print("Making Object")
    obj = Employee()
    print("Function End")
    return obj

print("Calling create_obj function")
obj = create_obj()
print("Program End")
