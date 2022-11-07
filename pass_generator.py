import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_legth = int(input("How long would you like your password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(password_legth):
        password.append(random.choice(characters))

    #random.shuffle(password)

    password = "".join(password)
    print(f"Your password is: {password}")

option = input("Do yo want to generate a password? (Yes/No): ")

if option == "yes" or option == "Yes":
    generate_password()
elif option == "no" or option == "No":
    print("Program ended")
    quit()
else:
    print("Invalid input! Please input Yes or No")