hs = [12,79,56,84,35]
hs1 = sorted(hs,reverse = True)
for i in range(0,len(hs1)):
    print("Hiscores:")
    print(i+1, " . ", hs1[i])
while True:
    hs.append(int(input("Enter new highscores")))
    hs1 = sorted(hs,reverse = True)
    for i in range(0,5):
        print("Hiscores:")
        print(i+1, " . ", hs1[i])
    con=input("Continue? y/n")
    if con == "n":
        break