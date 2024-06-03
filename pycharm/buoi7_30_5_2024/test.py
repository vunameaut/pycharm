import random
from turtle import  *

def cau1():
    windown =Screen()
    control =Turtle()
    control.speed(50)

    control.color("red", "white")
    control.pensize(30)

    control.begin_fill()

    for i in range(4):
        control.forward(200)
        control.left(90)

    control.end_fill()


    control.hideturtle()

    windown.mainloop()

def cau2():
    window = Screen()
    control = Turtle()
    control.speed(50)
    control.goto(0,0)
    control.pensize(3)


    control.color("red")
    for i in range(4):
        control.forward(200)
        control.left(90)
    control.penup()
    control.goto(200,70)
    control.pendown()
    control.color("white")
    control.left(90)
    control.forward(38)

    control.color("red")
    control.right(90)
    control.forward(50)

    control.left(90)
    control.forward(50)

    control.right(135)
    control.forward(90)

    control.right(90)
    control.forward(90)

    control.right(135)
    control.forward(40)

    control.left(90)
    control.forward(50)

    control.penup()
    control.goto(80,90)
    control.pendown()
    control.right(135)

    control.begin_fill()
    control.forward(50)
    control.right(90)
    control.forward(50)
    control.right(135)
    control.forward(70)
    control.end_fill()


#vẽ ô tô

    control.penup()
    control.goto(-300,130)
    control.pendown()
    control.right(180)
    control.color("green")
    control.begin_fill()
    control.forward(200)
    control.right(90)
    control.forward(50)
    control.left(90)
    control.forward(50)
    control.right(90)
    control.forward(50)
    control.right(90)
    control.forward(250)
    control.right(90)
    control.forward(100)
    control.end_fill()

#vẽ bánh
    control.penup()
    control.goto(-250,10)
    control.pendown()
    control.color("blue")
    control.pensize(10)
    control.circle(15)

    control.penup()
    control.goto(-100, 10)
    control.pendown()
    control.color("blue")
    control.pensize(10)
    control.circle(15)


# vẽ cửa xổ
    control.penup()
    control.goto(-180, 60)
    control.pendown()
    control.color("red")

    control.begin_fill()

    control.pensize(1)
    control.forward(35)
    control.right(90)
    control.forward(20)
    control.left(90)
    control.forward(10)
    control.left(90)
    control.forward(10)
    control.right(135)
    control.forward(20)
    control.right(90)
    control.forward(20)
    control.right(135)
    control.forward(10)
    control.left(90)
    control.forward(10)
    control.left(90)
    control.forward(20)
    control.right(90)
    control.forward(35)
    control.right(90)
    control.forward(50)


    control.penup()
    control.goto(-280, 60)
    control.right(90)
    control.pendown()
    control.pensize(1)
    control.forward(35)
    control.right(90)
    control.forward(20)
    control.left(90)
    control.forward(10)
    control.left(90)
    control.forward(10)
    control.right(135)
    control.forward(20)
    control.right(90)
    control.forward(20)
    control.right(135)
    control.forward(10)
    control.left(90)
    control.forward(10)
    control.left(90)
    control.forward(20)
    control.right(90)
    control.forward(35)
    control.right(90)
    control.forward(50)

    control.end_fill()







    control.hideturtle()
    window.mainloop()
def cau3():
    w = Screen()
    c = Turtle()
    c.speed(500)

    c.begin_fill()
    c.color("violet")
    c.goto(0,0)
    c.left(50)
    c.forward(133)
    c.circle(50, 200)
    c.right(140)
    c.circle(50, 200)
    c.forward(133)
    c.end_fill()

    c.penup()
    c.begin_fill()
    c.goto(100,0)
    c.left(52)
    c.pendown()
    c.color("green")
    c.left(50)
    c.forward(133)
    c.circle(50, 200)
    c.right(140)
    c.circle(50, 200)
    c.forward(133)
    c.end_fill()

    w.mainloop()




def cau4():
    w = Screen()
    c = Turtle()
    c.speed(50)

    c.penup()
    c.goto(-100, -100)
    c.pendown()
    c.color("red")

    c.begin_fill()
    for i in range(2):
        c.forward(200)
        c.left(90)
        c.forward(30)
        c.left(90)
    c.penup()
    c.goto(-15, -180)
    c.pendown()
    c.end_fill()
    c.begin_fill()
    for i in range(2):
        c.forward(30)
        c.left(90)
        c.forward(200)
        c.left(90)

    c.end_fill()
#vẽ dấu chia
    c.penup()
    c.goto(200, -100)
    c.pendown()
    c.color("green")

    c.begin_fill()
    for i in range(2):
        c.forward(200)
        c.left(90)
        c.forward(30)
        c.left(90)
    c.end_fill()

    c.begin_fill()
    c.penup()
    c.goto(300, -150)
    c.pendown()

    c.circle(23)
    c.end_fill()

    c.begin_fill()
    c.penup()
    c.goto(300, -63)
    c.pendown()

    c.circle(23)
    c.end_fill()


# vẽ dấu nhân

    c.penup()
    c.goto(-400, -150)
    c.pendown()
    c.left(45)
    c.color("yellow")

    c.begin_fill()
    for i in range(2):

        c.forward(200)
        c.left(90)
        c.forward(30)
        c.left(90)
    c.penup()

    c.goto(-300, -150)
    c.pendown()
    c.end_fill()
    c.begin_fill()
    for i in range(2):
        c.forward(30)
        c.left(90)
        c.forward(200)
        c.left(90)

    c.end_fill()





    c.hideturtle()
    w.mainloop()

def cau5():
    w = Screen()
    c = Turtle()
    c.speed(500)

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

#cờ
    c.color("red")
    c.begin_fill()
    c.left(155)
    c.forward(200)
    for i in range(4):
        c.forward(165)
        c.right(90)
    c.end_fill()
#ngoi sao

    c.penup()
    c.color("yellow")
    c.begin_fill()
    c.goto(210,250)
    c.right(20)
    c.pendown()
    for i in range(5):
        c.forward(100)
        c.right(144)

    c.end_fill()
    c.penup()
    c.color("black")
    c.goto(260,285)

    c.pendown()
    c.color("yellow")
    c.begin_fill()
    c.circle(19)
    c.end_fill()



#vẽ cánh cửa
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

    c.hideturtle()
    w.mainloop()


def cau6():
    w = Screen()
    c = Turtle()
    c.speed(50)

# hình cái bàn
    #c.pensize(10)
    c.color("#ac7339")

    c.goto(-300,0)
    c.begin_fill()
    c.forward(300)
    c.left(60)
    c.forward(200)
    c.left(120)
    c.forward(300)
    c.left(60)
    c.forward(200)
    c.left(30)
    c.forward(300)
    c.end_fill()


    c.penup()
    c.goto(0, 0)
    c.pendown()
    c.left(0)
    c.forward(300)


    c.penup()
    c.goto(100, 170)
    c.pendown()
    c.forward(300)

    c.penup()
    c.goto(-200,0)
    c.pendown()
    c.forward(200)

    c.pensize(1)



    c.goto(-130,150)
    c.color("#99b3e6")
    c.begin_fill()
    c.pendown()
    c.left(180)
    c.forward(50)
    c.left(90)
    c.forward(100)
    c.right(90)
    c.forward(100)
    c.right(90)
    c.forward(300)
    c.right(90)
    c.forward(100)
    c.right(90)
    c.forward(100)
    c.left(90)
    c.forward(50)
    c.right(90)
    c.forward(100)
    c.end_fill()


#ve mat cuoi
    c.color("#ffb3b3")
    c.begin_fill()
    c.penup()
    c.goto(-80,270)
    c.pendown()
    c.circle(40)
    c.end_fill()

    c.color("black")
    c.begin_fill()
    c.penup()
    c.goto(-100,250)
    c.pendown()
    c.circle(5)
    c.end_fill()
    c.begin_fill()

    c.penup()
    c.goto(-60, 250)
    c.pendown()
    c.circle(5)
    c.end_fill()
    c.begin_fill()
    c.penup()
    c.goto(-90, 220)
    c.pendown()
    c.end_fill()
    c.begin_fill()
    c.left(90)
    c.circle(10,200)
    c.end_fill()


    c.penup()
    c.color("black")
    c.goto(-200, 50)
    c.begin_fill()
    c.pendown()
    c.right(110)
    c.forward(150)
    c.left(60)
    c.forward(100)
    c.left(120)
    c.forward(150)
    c.left(60)
    c.forward(100)
    c.end_fill()

#hình nón

    c.color("yellow")
    c.begin_fill()
    c.penup()
    c.goto(-120, 260)
    c.pendown()
    c.right(200)
    c.forward(60)
    c.right(90)
    c.forward(60)

    c.penup()
    c.goto(-120, 260)
    c.pendown()
    c.right(45)
    c.circle(40,200)



#vẽ lọ hoa
    c.penup()
    c.color("brown")
    c.goto(200, 60)
    c.pendown()
    c.left(165)
    #hoa1

    c.begin_fill()
    for i in range(2):
        c.forward(150)
        c.left(90)
        c.forward(70)
        c.left(90)
    c.end_fill()
    c.color("pink")
    c.begin_fill()
    c.penup()
    c.goto(230, 100)
    c.pendown()
    c.right(180)
    c.circle(20,170)
    for i in range(8):
        c.circle(20,170)
        c.right(120)

    c.end_fill()
    c.color("brown")
    c.penup()
    c.goto(230, 100)
    c.right(30)
    c.pendown()
    c.forward(39)







    c.hideturtle()
    w.mainloop()





while True:
    chon=int(input("nhập vào lựa chọn của bạn: "))
    match(chon):
        case 1:
            cau1()
        case 2:
            cau2()
        case 3:
            cau3()
        case 4:
            cau4()
        case 5:
            cau5()
        case 6:
            cau6()
        case 7:
            break