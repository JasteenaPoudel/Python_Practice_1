name = "Global"

def show_scope():
    name = "Local"
    print("Inside functions:", name)


show_scope()
print("Outside functions:",name)

age = 19

def show_age():
    age = 25
    print("inside the function the age :",age)


show_age()
print("Outside the function:",age)