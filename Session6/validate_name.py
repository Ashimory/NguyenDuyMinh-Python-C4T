while True:
    name = input("Enter your name", )
    if name.isalpha():
        print("User's name acquired,", name)
        break
    else:
        print("Please retry")
