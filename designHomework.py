from turtle import*



title("myDesignProject")
setup(width = 600, height = 1000)
bgcolor("beige")
speed(30)

def startDraw(c,x,y):
    penup()
    goto(x,y)
    pendown()
    color(c)
    begin_fill()

def Rose():
    left(45)
    forward(50)
    circle(40,180)
    forward(50)
    right(135)
    forward(50)
    circle(40,180)
    forward(50)
    right(135)
    forward(50)
    circle(40,180)
    forward(50)
    right(45)
    forward(100)
    circle(97,180)
    forward(100)
    end_fill()

def sunSet():
    circle(50,180)
    end_fill()

def stick():
    setheading(0)
    right(80)
    for i in range(100):
        right(0.4)
        forward(4)
    circle(10,180)
    for i in range(100):
        left(0.4)
        forward(4)
        if(i == 50):
            right(160)
            circle(60,180)
            circle(20,-180)
            circle(-40,-170)
            setheading(80)
    circle(8,180)
    end_fill()

startDraw("red",70,300)
Rose()
startDraw("yellow",25,280)
sunSet()
startDraw("orange",-75,280)
sunSet()
startDraw("green",-30,105)
stick()

hideturtle()
mainloop()
