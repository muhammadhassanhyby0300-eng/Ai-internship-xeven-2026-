grade_input = input("Enter your grade (0-100): ")
if grade_input.isdigit():
    grade = int(grade_input)  
    if grade < 0 or grade > 100:
        print("Grade must be between 0 and 100.")
    elif grade >= 90:
        print("Grade: A - Excellent work!")
    elif grade >= 80:
        print("Grade: B - Good job!")
    elif grade >= 70:
        print("Grade: C - Keep improving!")
    elif grade >= 60:
        print("Grade: D - Needs more effort.")
    else:
        print("Grade: F - Don't give up, keep trying!")
else:
    print("Invalid input. Please enter a numeric grade.")
