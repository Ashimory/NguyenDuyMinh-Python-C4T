while True:
    count = 0
    x = int(input("Enter a number"))
    while x>0:
        x//=10
        count+=1
    print("The number has", count, "digit")
    

