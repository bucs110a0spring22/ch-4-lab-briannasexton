import turtle
import math
import random
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help




def setupWindow(window):
  '''
  sets up viewing window for graph and sets color 
  '''
  leo = turtle.Turtle()
  window.bgcolor("pink")
  window.setworldcoordinates(-360,-1,360,1)
  leo.speed(3)

def setupAxis(leo):
  '''
  sets up x and y axis for graphs to be drawn on
  '''
  leo.goto(-360,0)
  leo.goto(360,0)
  leo.goto(0,0)
  leo.goto(0,1)
  leo.goto(0,-1)
  leo.penup()

def drawSineCurve(myturtle=None):
  '''
  draws a sin curve and established turtle
  '''
  leo = turtle.Turtle()
  leo.speed(3)
  for angle in range(-360,360):
    graph=math.sin(math.radians(angle))
    leo.goto(angle,graph)
    leo.pendown()
  leo.penup()
  leo.clear()
  
def drawCosineCurve(leo):
  '''
  turtle draws cosine function on graph
  '''
  leo.penup()
  for angle in range(-360,360):
    i=math.cos(math.radians(angle))
    leo.goto(angle,i)
    leo.pendown()
  leo.penup()
  leo.clear()

def drawTangentCurve(leo):
  '''
  turtle draws tangent function on graph
  '''
  leo.penup()
  for angle in range(-360,360):
    i=math.tan(math.radians(angle))
    leo.goto(angle,i)
    leo.pendown()
  leo.penup()
  leo.clear()

def guessCurve(leo):
  leo = turtle.Turtle()
  leo.penup()
  leo.pendown()
  #my_list = [drawSineCurve(leo),drawCosineCurve(leo),drawTangentCurve(leo)]
  Sine = drawSineCurve(leo)
  Cosine = drawCosineCurve(leo)
  Tangent = drawTangentCurve(leo)
  my_list = [Sine, Cosine, Tangent]
  function = random.choice(my_list)
  for i in (my_list):
    guess = str(input("Please enter which curve this is:"))
    if guess == function:
        print("Correct!")
    elif guess!= function:
        print("Incorrect! Correct answer is:")
        print(function)


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
    guessCurve(dart)
    wn.exitonclick()
main()
