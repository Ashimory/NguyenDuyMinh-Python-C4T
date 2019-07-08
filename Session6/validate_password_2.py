while True:
    name = input("Enter your password", )
    if name.isalpha():
        print("Please retry")
    elif len(name) > 8:
        print("Login successful")
        break
    else:
        print("Please retry")
        