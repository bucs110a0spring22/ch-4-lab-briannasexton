import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
leo = turtle.Turtle()

def drawSineCurve(leo):
  for angle in range(-360,360):
    i=math.sin(math.radians(angle))
    leo.goto(angle,i)
    leo.pendown()
  leo.penup()

def setupWindow(window):
  window.bgcolor("pink")
  window.setworldcoordinates(-360,-1,360,1)
  leo.speed(3)
def setupAxis(leo):
  leo.goto(-360,0)
  leo.goto(360,0)
  leo.goto(0,0)
  leo.goto(0,1)
  leo.goto(0,-1)
  leo.penup()


def drawCosineCurve(leo):
  leo.penup()
  for angle in range(-360,360):
    i=math.cos(math.radians(angle))
    leo.goto(angle,i)
    leo.pendown()
  leo.penup()

def drawTangentCurve(leo):
  leo.penup()
  for angle in range(-360,360):
    i=math.tan(math.radians(angle))
    leo.goto(angle,i)
    leo.pendown()
  leo.penup()

##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
