from turtle import *
shape("turtle")
color("cyan")
speed(-1)
for i in range(12):
    if i in range(4):
        forward(100)
        left(90)
    elif i in range(7):
        forward(100)
        left(120)
    else:
        forward(100)
        left(72)

mainloop()