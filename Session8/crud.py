import re
items = ["ayy", "bee", "see"]
while True:
    do = input("Enter c to add to the list, r to read the list, u to update the list, d to delete an item. Enter ok to finish ")
    if do == "c":
        add = input("What do you want to add to the list? ")
        items.append(add)
        print("The list is now",(*items))
    if do == "r":
        if items:
            print(*items, sep = "\n" )
        else:
            print("The list is empty")
    if do == "u":
        up = int(input("Which position do you want to update? "))
        content = input("New content? ")
        items[up - 1] = content
        print("The list is now",(*items))
    if do == "d":
        delete = int(input("Which position do you want to delete? "))
        items.pop(delete - 1)
        print("The list is now",(*items))
    if do == "ok":
        print("The final list is ", items)
        break