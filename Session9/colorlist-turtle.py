from turtle import *
colors = ["red","green","blue","yellow"]
count = 0
for i in range (4):
    color(colors[count])
    forward(100)
    count +=1

mainloop()