import random
import re
count = 0
while True:
    num1 = random.randint(1,30)
    num2 = random.randint(1,30)
    if random.randint(0,1):
        op = "+"
    else:
        op = "-"
    if random.randint(0,1):
        ans = random.randint(1,100)
    else:
        if op == "+":
            ans = num1 + num2
        else:
            ans = num1 - num2
    print (num1,op,num2,"=",ans)
    while True:
        tf = input ("t for true, f for false, or x to quit")
        if not re.match("t", tf) and not re.match("f", tf) and not re.match("x", tf):
            print("INPUT ERROR: Enter t or f to answer, or x to quit")
        else:
            break
    if op == "+":
        if ans == num1 + num2:
            correct = "t"
        else:
            correct = "f"
    if op == "-":
        if ans == num1 - num2:
            correct = "t"
        else:
            correct = "f"
    if tf == correct:
        count += 1
        print("Score:", count)
    else:
        print("Game Over")
        break
