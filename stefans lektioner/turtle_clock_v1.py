import turtle
import time

def moveto(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def home():
    moveto(0,0)

def drawFace(radius, width, color):
    moveto(0,-radius)
    turtle.setheading(0)
    turtle.circle(radius)
    turtle.color(color)
    turtle.width(width)
    
def drawDots():
    pass

def drawHand(lenght, angle, width, color):
    home()
    turtle.color(color)
    turtle.width(width)
    turtle.setheading(angle)
    turtle.forward(lenght)

turtle.setup(800,600)
turtle.bgcolor("#00ff00")
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0)

s = -1

Running = 1

while (Running == True):

    sPrev = s

    while (s == sPrev):
        now =time.localtime()
        h = now.tm_hour
        m = now.tm_min
        s = now.tm_sec
        time.sleep(0.01)
    
    turtle.clear()
    drawFace(260, 9, "#000000")
    drawHand(245, 90-6*s, 4, "#000000")
    drawHand(200, 90-6*m-0.1*1*s, 5, "#000000")
    drawHand(150, 90-30*h-0.1*m, 6, "#000000")


    turtle.update()
    
    

    
   
