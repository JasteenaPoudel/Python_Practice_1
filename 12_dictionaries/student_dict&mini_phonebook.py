student = {
    "Name":"Riyu Pokharel",
    "Age":20,
    "GPA":3.80,
    "Subject":"TOC"
}

print("====================")
print("Student description")
print("====================")
print("Name:",student["Name"])
print("Age:",student["Age"])
print("Gpa:",student["GPA"])
print("subject:",student["Subject"])
print("====================")


phonebook = {
    "ram" : "9841xxxxxxx",
    "Hari":"9843xxxxxxxx"
}

# Search the contact
search_name = input("Enter a name to be searched:")

if search_name in phonebook:
    print(search_name, ":", phonebook[search_name])

else:
    print("Contact not found")

# add new contact
# Add new contact
new_name = input("Enter new contact name: ")
new_number = input("Enter phone number: ")

phonebook[new_name] = new_number

# print all contents
print("\n All contacts:")
for name, number in phonebook.items():
    print(name, ":", number)
