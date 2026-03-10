username= input("Enter your username: ")
password= input("Enter your password: ")
age= int(input("Enter your age: "))
if len(username)< 5:
    print("Username must be at least 5 characters long.")
elif len(password)< 8:
    print("Password must be at least 8 characters long.")
elif age <= 18:
    print("Age must be 18 or above.")
else:
    print("Access granted! Welcome, ",username)