# Requirements

# Create student list.

# Program should:

# add student
# remove student
# print all students
# count students

# student_manager.py

students = []

while True:
    print("\n===== STUDENT MANAGER =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Print All Students")
    print("4. Count Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add student
    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print(name, "added successfully!")

    # Remove student
    elif choice == "2":
        name = input("Enter student name to remove: ")

        if name in students:
            students.remove(name)
            print(name, "removed successfully!")
        else:
            print("Student not found!")

    # Print all students
    elif choice == "3":
        if len(students) == 0:
            print("No students in the list.")
        else:
            print("\nStudent List:")
            for student in students:
                print("-", student)

    # Count students
    elif choice == "4":
        print("Total students:", len(students))

    # Exit program
    elif choice == "5":
        print("Exiting program...")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please try again.")