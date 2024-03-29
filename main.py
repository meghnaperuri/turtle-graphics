# # from turtle import Turtle, Screen
# #
# # lola=Turtle()
# # screen=Screen()
# #
# # def move_forward():
# #     lola.forward(10)
# #
# # screen.listen()
# # screen.onkey(key="space", fun=move_forward)
# # screen.exitonclick()
# #--------------------ETCH A SKETCH--------------------------
# from turtle import Turtle,Screen
#
# lola=Turtle()
# screen=Screen()
#
# def move_forward():
#     lola.forward(10)
#
# def move_backward():
#     lola.setheading(180)
#     lola.forward(10)
#
# def turn_right():
#     lola.right(10)
#
# def turn_left():
#     lola.left(10)
#
# def clear():
#     lola.clear()
#     lola.penup()
#     lola.home()
#     lola.pendown()
#
# screen.listen()
# screen.onkey(key="w",fun=move_forward)
# screen.onkey(key="s",fun=move_backward)
# screen.onkey(key="a",fun=turn_right)
# screen.onkey(key="d",fun=turn_left)
# screen.onkey(key="c",fun=clear)
#
# screen.exitonclick()
# #---------------------TURTLE RACE-------------------------

from turtle import Turtle,Screen
import random


screen=Screen()
screen.setup(width=500,height=400)
userBet=screen.textinput("place a bet","who are you going to bet on?")
print(userBet)

lola=Turtle(shape="turtle")
timmy=Turtle(shape="turtle")
tommy=Turtle(shape="turtle")
bella=Turtle(shape="turtle")
stark=Turtle(shape="turtle")

colors=["red","green","blue","purple","coral"]
objectList=[lola,timmy,tommy,bella,stark]
ycord=[-20,-0,20,40,60]
xcord=[-230,-230,-230,-230,-230]
race_on=False
all_turtles=[]
def moveforward():
    highestxcord=0
    color=""
    for i in range(0,len(objectList)):
        objectList[i].penup()
        objectList[i].goto(xcord[i], ycord[i]*2 )
        objectList[i].color(colors[i])
    global race_on
    # race_on = False
    if userBet:
        race_on=True
    while race_on:
        for turtle in objectList:
            if turtle.xcor()<=230:
                # print(turtle.color())
                turtle.forward(random.randint(0,11))
            x, y = turtle.pos()
            if int(x)>230:
                race_on=False
            if turtle.xcor()>highestxcord:
                highestxcord=turtle.xcor()
                color=turtle.color()
                # print(color[0])
    if color and color[0]==userBet:
        print("you won")
    else:
        print("you lost")
            # print(x,y)

screen.listen()
screen.onkey(key="space",fun=moveforward)

screen.exitonclick()

