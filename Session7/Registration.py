user = input("Enter your username ")
while True:
    email = input("Enter your email ")
    if "@" in email:
        if "." in email:
            break
        else:
            print("Please retry")
    else:
            print("Please retry")

while True:
    password = input("Enter your password ")
    if not password.isalpha() and not password.isdigit() and len(password)>8 and ("@") in password and (".com")  in password :
        break
    else:
        print("Please retry")
while True:
    re = input("Re-enter password ")
    if password == re: 
        print ("Login success!")
        break
    else:
        print ("Please retry")


        
