from turtle import  *

windown = Screen()
control = Turtle()
control.speed(50)

control.color("red", "white")
control.pensize(1)

control.begin_fill()

angle = 180 - (360 / 6)

# Vẽ ngôi sao
for i in range(6):
    control.forward(100)
    control.right(angle)

control.end_fill()

control.hideturtle()

windown.mainloop()