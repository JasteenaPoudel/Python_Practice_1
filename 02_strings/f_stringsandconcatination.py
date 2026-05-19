name = "Jasteena"
age = 19

print(f"Hello, my name is {name}")

print(f"I am {age} years old")

city = "Kathmandu"
country = "Nepal"

print(f"I live in {city},{country}")

name = input("Enter ur name:")
print("Welcome",name)

first_msg = "Hy,"
second_msg = "How are you?"
print(first_msg + second_msg)

# Exercise

# Create:

# first_name
# last_name

# Join them into full name.

first_name = "Jasteena"
last_name = "Poudel"

print(first_name + last_name)

# Challenge

# Try:

# "Age: " + 19

# Observe the error.

# Now fix it using:

# str()
# f-string
print("Age:" + 19)
# TypeError: can only concatenate str (not "int") to str

print("age:" + str(19))

print(f"Age: {age}")
