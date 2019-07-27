while True:
    init = input("Type start to begin quiz, quit to end")
    if init.lower() == "start":
        print("Ok")
    elif init.lower() == "quit":
        print ("Bye")
        break
    correct = ["1","2","3","4"]
    questions = ["Was Mega Sceptile introduced in ORAS?", 
    "What is Sceptile's first type?", 
    "What is Sceptile's second type?", 
    "Which move can Sceptile learn?"]
    answers = ["1: Yes, 2: No", 
    "1: Fire, 2: Grass, 3: Water",
    "1: Psychic, 2: Dark, 3: Dragon, 4: Fairy", 
    "1: Fire Blast, 2: Hydro Pump, 3: Dark Pulse, 4: Hidden Power"]
    count = 0
    for i in range(0, len(questions)):
        print(questions[i])
        ans = input(answers[i])
        if ans == correct[i]:
            count += 1
    percentage = count / len(questions) * 100
    print("You got", count, "questions right,", percentage, "% of questions")


