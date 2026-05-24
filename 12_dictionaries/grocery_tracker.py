# Features:

# add grocery
# update quantity
# print all groceries

# Grocery dictionary
groceries = {
    "apple": 5,
    "banana": 12
}

# Add grocery
item = input("Enter item to add: ")
quantity = int(input("Enter quantity: "))

groceries[item] = quantity

# Update quantity
update_item = input("Enter item to update: ")

if update_item in groceries:
    new_quantity = int(input("Enter new quantity: "))
    groceries[update_item] = new_quantity
else:
    print("Item not found!")

# Print all groceries
print("\nAll Groceries:")

for item, quantity in groceries.items():
    print(item, ":", quantity)

# Print:

# name
# all subjects
# first subject

# Add another subject.

student = {
    "name": "Jasteena",
    "subjects": ["Python", "Math", "DBMS"]
}
print(student["name"])
print(student["subjects"])
print(student["subjects"][0])

student["subjects"].append("TOC")
print(student)