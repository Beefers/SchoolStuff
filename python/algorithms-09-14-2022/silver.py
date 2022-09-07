# Prompt the user for input of personal details, verify them, and let the user continue if correct
username = "ethan"
password = "mypasswordisverysecure"
givenUsername = str(input("Enter your username: "))
givenPassword = str(input("Enter your password: "))

if (givenUsername != username): print("Your username is incorrect."); exit()
if (givenPassword != password): print("Your password is incorrect."); exit()

print("Logged in successfully!")