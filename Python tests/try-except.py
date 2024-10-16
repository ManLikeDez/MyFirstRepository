def safe_division():
    try:
        divisor = int(input("Enter a number to divide by: "))
        result = 10 / divisor
        print (f"The result is {result}.")
    except ZeroDivisionError:
        print ("Error: You can't divide by zero! ")
    except ValueError:
        print ("Error: Please enter a valid integer. ")

# To call the function
safe_division()

# Password login system

class LoginSystem:
    def create_user(self):
        username = str(input("Enter username to use please: "))
        password = str(input("Enter password to use, please: "))
        print(f"Your details are: Username {username} and Password {password}")
        return True  # Indicate success
    


Computer = LoginSystem()
Computer.create_user()




