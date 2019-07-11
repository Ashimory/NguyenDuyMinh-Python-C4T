numlist = ["1", "312", "543", "4"]
num = input("Enter number")
if num in numlist:
    pos = int(numlist.index(num)) + 1
    print("The number is at position", pos)
else:
    print("Not on our  list!")