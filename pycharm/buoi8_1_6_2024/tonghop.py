from turtle import  *



w = Screen()
c =Turtle()

c.pensize(0)

w.bgcolor('black')
c.width(3)
c.speed(25)

color = ('magenta', 'yellow', 'green')
for i in range(500):
    c.pencolor(color[i%3])
    c.forward(i*4)
    c.right(121)


c.hideturtle()

w.mainloop()














