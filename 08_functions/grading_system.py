def calculate_grade(marks):
    

    if (marks >= 90):
        print("Your Grade is A+")
    elif(marks >=80):
        print("Your Grade is B")
    elif(marks >=70):
        print("Your Grade is C")
    else:
        print("You are Failed")

marks = (int(input("Enter the grade of the students:")))

calculate_grade(marks)