import turtle
import math
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
  args: int
  return:none
  '''
  leo.goto(-360,0)
  leo.goto(360,0)
  leo.goto(0,0)
  leo.goto(0,1)
  leo.goto(0,-1)
  leo.penup()

def Color(leo):
  '''
  lets user chose color
   args: str
  return:none
  '''
  chosen_color = str(input("please enter a color:"))
  leo.color(chosen_color)

def drawSineCurve(lee):
  '''
  draws a sin curve and established turtle
  args: int
  return:none
  '''
  leo = turtle.Turtle()
  leo.speed(3)
  leo.penup()
  for angle in range(-360,360):
    graph=math.sin(math.radians(angle))
    leo.goto(angle,graph)
    leo.pendown()
  leo.penup()
  
  
def drawCosineCurve(leo):
  '''
  turtle draws cosine function on graph
  args: int
  return:none
  '''
  leo.penup()
  for angle in range(-360,360):
    i=math.cos(math.radians(angle))
    leo.goto(angle,i)
    leo.pendown()
  leo.penup()
  

def drawTangentCurve(leo):
  '''
  turtle draws tangent function on graph
  args: int
  return:none
  '''
  leo.penup()
  for angle in range(-360,360):
    i=math.tan(math.radians(angle))
    leo.goto(angle,i)
    leo.pendown()
  leo.penup()
  




def guessNumber(leo):
  ''' 
  allows user to guess number of graphs drawn
  args: int
  return:str
  '''
  number_graphs = int(3)
  guess = int(input("How Many Graphs Were Drawn?"))
  if guess == number_graphs:
    print("True!")
    Star(leo)
  elif guess != number_graphs:
    print("False!")



def Star(leo):
  color= ['yellow','orange','green','cyan','blue']
  turtle.pensize(4)
  turtle.penup()
  turtle.setpos(-90,30)
  turtle.pendown()
  for i in range(5):
      turtle.pencolor(color[i])
      turtle.forward(200)
      turtle.right(144)
 
  turtle.penup()
  turtle.setpos(80,-140)
  turtle.pendown()
  turtle.pencolor("Black")
  turtle.done()
  



##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)
    dart.clear()

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    Color(dart)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    guessNumber(dart)
    dart.clear()
    dart.reset()
    #Star(dart)
    wn.exitonclick()
    
main()

