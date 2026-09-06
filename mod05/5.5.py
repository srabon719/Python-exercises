attempts = 0
login_successful = False

while attempts < 5 and login_successful == False:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "python" and password == "rules":
        login_successful = True
    else:
        attempts = attempts + 1

if login_successful == True:
    print("Welcome")
else:
    print("Access denied")