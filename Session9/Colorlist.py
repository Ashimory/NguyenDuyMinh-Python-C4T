colors = ["red","green","blue","yellow"]
print("Current color list:")
print(*colors, sep = ",")
add = input("Add a color: ")
colors.append(add)
print("Current color list:")
print(*colors, sep = ",")
pos = int(input("Select a position"))
print("The color in that position is",colors[pos-1])
delete = input("Choose color to delete")
if delete.isdigit():
    print("Current color list:")
    colors.pop(int(delete) - 1)
    print(*colors, sep = ",")
else:
    print("Current color list:")
    colors.remove(delete)
    print(*colors, sep = ",")
