import turtle
import time

def main():
    '''
猫和老鼠游戏：
实验功能：
    用方向键控制老鼠，使其保持在猫的前方。
    由计算机控制猫
    保持时间越长，得分越高
'''


    boxsize = 300
    caught = False
    score = 0

# functions that are called on keypresses
    def up():
        mouse.forward(10)
        checkbound()

    def left():
        mouse.left(45)

    def right():
        mouse.right(45)

    def back():
        mouse.backward(10)
        checkbound()

    def quitTurtles():
        window.bye()

# stop the mouse from leaving the square set by box size

    def checkbound():
        global boxsize
        if mouse.xcor() > boxsize:
            mouse.goto(boxsize,mouse.ycor)
        if mouse.xcor() < -boxsize:
            mouse.goto(-boxsize,mouse.ycor)
        if mouse.ycor() > boxsize:
            mouse.goto(mouse.xcor,boxsize)
        if mouse.ycor() < -boxsize:
            mouse.goto(mouse.xcor,-boxsize)

# set up screen
    window = turtle.Screen()
    mouse = turtle.Turtle()
    cat = turtle.Turtle()
    mouse.penup()
    mouse.penup()
    mouse.goto(100,100)

# add key listeners
    window.onkeypress(up,"Up")
    window.onkeypress(left,"Left")
    window.onkeypress(right,"Right")
    window.onkeypress(back,"Down")
    window.onkeypress(quitTurtles,"Escape")

    difficulty = window.numinput('Difficulty','Enter a difficulty from easy (1),for hard (5)',minval = 1,maxval = 5)

    window.listen()

# main loop
# note how it change with difficulty
    while not caught:
        cat.setheading(cat.towards(mouse))
        cat.forward(8+difficulty)
        score = score + 1
        if cat.distance(mouse) < 5:
            caught = True
        time.sleep(0.2 - (0.01*difficulty))
    window.textinput('Game Over','Well done.You scored:'+ str(score*difficulty))
    window.bye()