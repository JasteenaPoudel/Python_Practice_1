def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}")

# Exercises
# Create profile function
# def create_profile(name, country="Nepal"):

# Example outputs:

# create_profile("Jasteena")
# → Name: Jasteena, Country: Nepal
# create_profile("Jasteena", "India")
# → Name: Jasteena, Country: India

def create_profile(name, country = "Nepal"):
    print(f"Name: {name}, Country: {country}")

create_profile("Riya")

create_profile("Sabnam", "Bangladesh")

def student_info(name,age,roll_no,college):
    print("Name:", name)
    print("Age:", age)
    print("Roll_no:", roll_no)
    print("Campus:", college)

student_info(name="Riya Pokharel", age = 20, roll_no = 14, college = "Butwal Multiple Campus")
student_info(name="Swikririti A.C.", age = 20, roll_no = 19, college = "Butwal Multiple Campus")

