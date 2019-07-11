from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
count = 0
for i in range(25):
    if i in range(3):
        color(colors[count])
        forward(100)
        left(120)
    elif i in range(7):
        color(colors[count + 1])
        forward(100)
        left(90)
    elif i in range(12):
        color(colors[count + 2])
        forward(100)
        left(72)
    elif i in range(18):
        color(colors[count + 3])
        forward(100)
        left(60)
    else:
        color(colors[count + 4])
        forward(100)
        left(180 - (900/7))
mainloop()