name=input("Enter your Name :")
age_input=input("Enter your age:")
if age_input.isdigit():
    age=int(age_input)
    if age<0:
        print("Kindy add a valid age")
    elif age<13:
        print(f"hello{name}! Enjoy your life child")
    elif age<=17:
        print(f"Hello {name}! enjoy your life as a Teenager")
    elif age<=64:
        print(f"Hello {name}! unfortunately You are an adult")
    else :
        print(f"Hello {name}! enjoy! You are a senior citizen")
else:    print("You are a monster or an alien")
