import random
player = {
    "Name" : "Ashimory",
    "Age" : 17,
    "Strength" : 8,
    "Defense" : 10,
    "HP": 100,
    "Backpack" : ["Sword", "Shield", "Bread Loaf", "Strange Locket"],
    "Gold" : 100,
    "Level" : 2,
}
player["Gold"] += 50
player["Backpack"].append("Flint Stone")
player["Pocket"]= ["Monster Dex", "Flashlight"]
# print(player)
skill1 = {
"Name": "Attack",
"Minimum level": 1,
"Damage": 5,
"Hit rate": 0.3,
}
skill2 = {
    "Name": "Quick Attack",
    "Minimum level": 2,
    "Damage": 3,
    "Hit rate": 0.5,
}
skill3 = {
    "Name": "Strong Kick",

    "Minimum level": 4,

    "Damage": 9,

    "Hit rate": 0.2,
}
skills = [skill1, skill2, skill3]
for i in range(0, len(skills)):
    print(i+1,".", skills[i]["Name"])
x = int(input("Choose your skill: ")) - 1
if not player["Level"] < skills[x]["Minimum level"]:
    hit = random.randint(0, 11) / 10
    if not hit > skills[x]["Hit rate"]:
        print(skills[x]["Damage"], "dmg dealt!")
    else:
        print("Missed!")
else:
    print("Insufficient level!")