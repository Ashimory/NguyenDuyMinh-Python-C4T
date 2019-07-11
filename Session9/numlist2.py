numlist = [1, 312, 543, 4]
i1 = sum (numlist)
print("The sum is", i1)
total = 0
for i in range(0,len(numlist)):
    total += numlist[i]
print("Method 2 gives the result of", total)