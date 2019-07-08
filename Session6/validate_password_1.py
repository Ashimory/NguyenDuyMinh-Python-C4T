while True:
    name = input("Enter your password", )
    if name.isalpha():
        print("Please retry")
    else:
        print("Login successful")
        break
