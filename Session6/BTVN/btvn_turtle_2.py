side = 100
from turtle import *
speed(-1)
left(240)
for i in range(50):
    right(10)
    for i in range (4):
        forward(side)
        right(90)
    side -=2

mainloop()