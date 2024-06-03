from turtle import  *



w = Screen()
c = Turtle()
c.speed(50)

goto(0,0)
c.color("#668cff")
c.begin_fill()
c.forward(120)
c.right(70)
c.forward(200)
c.right(110)
c.forward(250)
c.right(110)
c.forward(200)
c.end_fill()

c.color("#b34700")

c.penup()
c.goto(55,0)
c.pendown()
c.circle(70,80)

c.penup()
c.goto(20,125)
c.pendown()
c.right(90)
c.color("pink")
c.begin_fill()
for i in range(5):
    c.circle(20,200)
    c.right(120)
c.end_fill()

c.color("yellow")
c.begin_fill()
c.penup()
c.goto(18,105)
c.pendown()
c.circle(10)
c.end_fill()





c.hideturtle()

w.mainloop()














