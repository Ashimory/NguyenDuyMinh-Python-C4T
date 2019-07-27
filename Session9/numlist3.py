numlist = input("Enter list").split()
total = 0
for i in range(0,len(numlist)):
    total += int(numlist[i])
print("The sum is", total)