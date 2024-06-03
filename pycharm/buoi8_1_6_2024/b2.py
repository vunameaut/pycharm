from turtle import *


w = Screen()
c = Turtle()
c.speed(500000)


c.color("#4dd2ff")
c.begin_fill()
for i in range(4):
    c.forward(165)
    c.right(90)
c.end_fill()

c.color("#db70b8")
c.begin_fill()
c.left(60)
c.forward(180)
c.right(125)
c.forward(174)
c.end_fill()


# vẽ cánh cửa
c.left(135)
c.begin_fill()
c.penup()
c.goto(60, -165)
c.pendown()
c.color("brown")
c.left(20)

for i in range(2):
    c.forward(100)
    c.right(90)
    c.forward(50)
    c.right(90)
c.end_fill()




c.penup()
c.goto(500, -165)
c.pendown()

c.color("blue","blue")
c.left(90)
for i in range(4):
    c.begin_fill()

    c.forward(1000)
    c.left(90)
    c.forward(150)
    c.left(90)
    c.end_fill()

#mat troi
c.penup()
c.goto(330,330)
c.pendown()
c.color("yellow")
c.begin_fill()
c.circle(30)
c.end_fill()

c.penup()
c.goto(320,330)
c.right(90)
c.pendown()
c.forward(50)

c.penup()
c.goto(340,300)
c.pendown()
c.forward(50)

c.penup()
c.goto(320,285)
c.pendown()
c.forward(50)

c.color("black")
#cầu
c.penup()
c.goto(0, -165)
c.pendown()
c.right(180)
c.circle(300,30)

c.penup()
c.goto(170, -165)
c.pendown()
c.circle(500,25)

#cây

c.color("brown")
c.begin_fill()
c.penup()
c.goto(300, -165)
c.pendown()
c.left(125)
for i in range(2):
    c.forward(70)
    c.right(90)
    c.forward(10)
    c.right(90)

c.end_fill()
c.penup()
c.goto(330, -65)
c.pendown()
c.color("green")
c.begin_fill()
c.circle(30)
c.end_fill()


c.color("brown")
c.begin_fill()
c.penup()
c.goto(370, -165)
c.pendown()
for i in range(2):
    c.forward(70)
    c.right(90)
    c.forward(10)
    c.right(90)
c.end_fill()
c.penup()
c.goto(400, -65)
c.pendown()
c.color("green")
c.begin_fill()
c.circle(30)
c.end_fill()



c.color("brown")
c.begin_fill()
c.penup()
c.goto(-90, -165)
c.pendown()
for i in range(2):
    c.forward(70)
    c.right(90)
    c.forward(10)
    c.right(90)
c.end_fill()
c.penup()
c.goto(-60, -65)
c.pendown()

c.color("green")
c.begin_fill()
c.circle(30)
c.end_fill()

c.color("brown")
c.begin_fill()
c.penup()
c.goto(-180, -165)
c.pendown()
for i in range(2):
    c.forward(70)
    c.right(90)
    c.forward(10)
    c.right(90)
c.end_fill()
c.penup()
c.goto(-150, -65)
c.pendown()
c.color("green")
c.begin_fill()
c.circle(30)
c.end_fill()

c.color("brown")
c.begin_fill()
c.penup()
c.goto(220, -10)
c.pendown()
for i in range(2):
    c.forward(70)
    c.right(90)
    c.forward(10)
    c.right(90)
c.end_fill()
c.penup()
c.goto(250, 90)
c.pendown()
c.color("green")
c.begin_fill()
c.circle(30)
c.end_fill()


c.color("brown")
c.begin_fill()
c.penup()
c.goto(300, -10)
c.pendown()
for i in range(2):
    c.forward(70)
    c.right(90)
    c.forward(10)
    c.right(90)
c.end_fill()
c.penup()
c.goto(330, 90)
c.pendown()
c.color("green")
c.begin_fill()
c.circle(30)
c.end_fill()

#vẽ ô tô

c.penup()
c.left(90)
c.goto(-300, 130)
c.pendown()
c.right(180)
c.color("#ff80b3")
c.begin_fill()
c.forward(200)
c.right(90)
c.forward(50)
c.left(90)
c.forward(50)
c.right(90)
c.forward(50)
c.right(90)
c.forward(250)
c.right(90)
c.forward(100)
c.end_fill()

#vẽ bánh
c.penup()
c.goto(-250, 10)
c.pendown()
c.color("blue")
c.pensize(10)
c.circle(15)

c.penup()
c.goto(-100, 10)
c.pendown()
c.color("blue")
c.pensize(10)
c.circle(15)


# vẽ cửa xổ
c.penup()
c.goto(-180, 60)
c.pendown()
c.color("red")

c.begin_fill()

c.pensize(1)
c.forward(35)
c.right(90)
c.forward(20)
c.left(90)
c.forward(10)
c.left(90)
c.forward(10)
c.right(135)
c.forward(20)
c.right(90)
c.forward(20)
c.right(135)
c.forward(10)
c.left(90)
c.forward(10)
c.left(90)
c.forward(20)
c.right(90)
c.forward(35)
c.right(90)
c.forward(50)

c.penup()
c.goto(-280, 60)
c.right(90)
c.pendown()
c.pensize(1)
c.forward(35)
c.right(90)
c.forward(20)
c.left(90)
c.forward(10)
c.left(90)
c.forward(10)
c.right(135)
c.forward(20)
c.right(90)
c.forward(20)
c.right(135)
c.forward(10)
c.left(90)
c.forward(10)
c.left(90)
c.forward(20)
c.right(90)
c.forward(35)
c.right(90)
c.forward(50)

c.end_fill()


c.penup()
c.color("black")
c.goto(600, -10)
c.pendown()
c.forward(435)
c.penup()
c.goto(-0, -10)
c.pendown()
c.forward(440)








c.penup()
c.goto(-200, 300)
c.pendown()
c.color("#4da6ff")
c.begin_fill()
c.right(180)
c.circle(20)
c.end_fill()

c.penup()
c.goto(-220, 320)
c.pendown()
c.begin_fill()
c.right(180)
c.circle(20)
c.end_fill()

c.penup()
c.goto(-220, 300)
c.pendown()
c.begin_fill()
c.right(180)
c.circle(20)
c.end_fill()

c.penup()
c.goto(-180, 320)
c.pendown()
c.begin_fill()
c.right(180)
c.circle(20)
c.end_fill()





c.penup()
c.goto(-320, 320)
c.pendown()
c.begin_fill()
c.right(180)
c.circle(20)
c.end_fill()

c.penup()
c.goto(-320, 300)
c.pendown()
c.begin_fill()
c.right(180)
c.circle(20)
c.end_fill()

c.penup()
c.goto(-280, 320)
c.pendown()
c.begin_fill()
c.right(180)
c.circle(20)
c.end_fill()



#vẽ người

c.penup()
c.goto(0, -180)
c.pendown()
c.color("black")
c.begin_fill()
c.circle(10)
c.end_fill()

c.penup()
c.goto(0, -180)
c.pendown()
c.right(60)
c.forward(30)
c.right(45)
c.forward(20)
c.backward(20)
c.left(90)
c.forward(20)
c.penup()
c.goto(0,-180 - 15)
c.pendown()
c.right(75)
c.forward(20)
c.backward(20)
c.left(90)
c.forward(20)





c.penup()
c.goto(0, -220)
c.pendown()
c.color("black")
c.begin_fill()
c.circle(10)
c.end_fill()

c.penup()
c.goto(0, -220)
c.pendown()
c.right(60)
c.forward(30)
c.right(45)
c.forward(20)
c.backward(20)
c.left(90)
c.forward(20)
c.penup()
c.goto(0,-220 - 15)
c.pendown()
c.right(75)
c.forward(20)
c.backward(20)
c.left(90)
c.forward(20)



c.hideturtle()
























w.mainloop()