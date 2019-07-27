numlist = input("Enter numbers, seperated by a comma").split(",")
for num in numlist:
    if int(num) % 2 == 0:
        print(num,end=" ")
