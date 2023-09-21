from turtle import *

# Animals, from up to down: Panda, Cat and Sheep
def Panda():
    #The Panda
    goto(0,0)
    pendown()
    color("Black")
    circle(200)
    penup()
    #ears
    goto(-200,250)
    pendown()
    begin_fill()
    color("Black")
    circle(100)
    end_fill()
    penup()

    goto(200,250)
    pendown()
    begin_fill()
    color("Black")
    circle(100)
    end_fill()
    penup()
    #nose
    goto(0,100)
    pendown()
    begin_fill()
    color("Black")
    circle(30)
    end_fill()
    penup()

    #cheeks
    goto(-100,130)
    pendown()
    begin_fill()
    color("pink")
    circle(45)
    end_fill()
    penup()

    goto(100,130)
    pendown()
    begin_fill()
    color("pink")
    circle(45)
    end_fill()
    penup()
    #eyes
    goto(-88,155)
    pendown()
    begin_fill()
    color("Black")
    circle(45)
    end_fill()
    penup()

    goto(88,155)
    pendown()
    begin_fill()
    color("Black")
    circle(45)
    end_fill()
    penup()
    #big eye highlights
    goto(-80,189)
    pendown()
    begin_fill()
    color("white")
    circle(24)
    end_fill()
    penup()

    goto(80,189)
    pendown()
    begin_fill()
    color("White")
    circle(24)
    end_fill()
    penup()
    #small eye highlights
    goto(-100,163)
    pendown()
    begin_fill()
    color("White")
    circle(15)
    end_fill()
    penup()

    goto(100,163)
    pendown()
    begin_fill()
    color("White")
    circle(15)
    end_fill()
    penup()
    #mouth
    goto(-83,100)
    pensize(7)
    pendown()
    color("Black")
    right(90)
    circle(40, 180)
    penup()

    goto(0,100)
    pendown()
    color("Black")
    left(180)
    circle(40, 180)
    penup()

#==============================================================================

def Cat():
    #The Cat
    goto(0,0)
    pendown()
    begin_fill()
    color("#242526")
    circle(200)
    end_fill()
    penup()

    #ears
    goto(-190,240)
    pendown()
    begin_fill()
    color("#242526")
    goto(-250,400)
    goto(-90,340)
    goto(-190,240)
    end_fill()
    penup()

    goto(190,240)
    pendown()
    begin_fill()
    color("#242526")
    goto(250,400)
    goto(90,340)
    goto(190,240)
    end_fill()
    penup()

    goto(-190,260)
    pendown()
    begin_fill()
    color("#FCBACB")
    goto(-220,370)
    goto(-119,345)
    goto(-190,260)
    end_fill()
    penup()

    goto(190,260)
    pendown()
    begin_fill()
    color("#FCBACB")
    goto(220,370)
    goto(119,345)
    goto(190,260)
    end_fill()
    penup()

    #eyes
    goto(-100,150)
    pendown()
    begin_fill()
    color("Black")
    circle(45)
    end_fill()
    penup()

    goto(100,150)
    pendown()
    begin_fill()
    color("Black")
    circle(45)
    end_fill()
    penup()

    #big eye highlights
    goto(-105,190)
    pendown()
    begin_fill()
    color("white")
    circle(24)
    end_fill()
    penup()

    goto(105,190)
    pendown()
    begin_fill()
    color("White")
    circle(24)
    end_fill()
    penup()

    #small eye highlights
    goto(-100,153)
    pendown()
    begin_fill()
    color("White")
    circle(15)
    end_fill()
    penup()

    goto(100,153)
    pendown()
    begin_fill()
    color("White")
    circle(15)
    end_fill()
    penup()

    #nose
    goto(45,150)
    pendown()
    begin_fill()
    color("#FCBACB")
    goto(45,150)
    goto(-45,150)
    goto(0,100)
    end_fill()
    penup()

    #mouth
    goto(-83,100)
    pensize(7)
    pendown()
    color("Black")
    right(90)
    circle(40, 180)
    penup()

    goto(0,100)
    pendown()
    color("Black")
    left(180)
    circle(40, 180)
    penup()

#============================================================================

def Sheep():
    #The Sheep

    #legs
    penup()
    goto(250,25)
    pendown()
    begin_fill()
    color("black")
    goto(250,25)
    goto(250,-50)
    goto(275,-50)
    goto(275,25)
    end_fill()
    penup()

    penup()
    goto(125,25)
    pendown()
    color("black")
    begin_fill()
    goto(125,25)
    goto(125,-50)
    goto(150,-50)
    goto(150,25)
    end_fill()
    penup()

    #body
    penup()
    goto(275,100)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(250,100)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(210,105)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(170,100)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(130,105)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(90,90)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()
    #break
    penup()
    goto(80,70)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(120,70)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(160,70)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(200,70)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(240,70)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(275,70)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()
    #break

    penup()
    goto(250,50)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(210,50)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(170,50)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(125,50)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(80,50)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(275,50)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()
    #break

    penup()
    goto(275,30)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(90,30)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(125,30)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(170,30)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(210,30)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(250,30)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(275,30)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()
    #break

    penup()
    goto(125,15)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(170,15)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(210,15)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(220,15)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(250,15)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    penup()
    goto(275,15)
    pendown()
    begin_fill()
    color("#d3d3d3")
    circle(25)
    end_fill()
    penup()

    #head
    penup()
    goto(300,30)
    pendown()
    begin_fill()
    color("black")
    circle(50)
    end_fill()
    penup()

    #eyes
    goto(275,70)
    pendown()
    begin_fill()
    color("white")
    circle(15)
    end_fill()
    penup()

    goto(325,70)
    pendown()
    begin_fill()
    color("white")
    circle(15)
    end_fill()
    penup()

    goto(275,80)
    pendown()
    begin_fill()
    color("black")
    circle(8)
    end_fill()
    penup()

    goto(325,80)
    pendown()
    begin_fill()
    color("black")
    circle(8)
    end_fill()
    penup()

#============================================================================

#Vehicles

def Truck():
    #The Truck
    #goto(-40, 85)
    #wheels
    #body
    #details
    write("Truck under construction!", font=("Verdana", 15, "normal"))

def Car():
    #The Car
    #goto(-40, 85)
    #Wheels
    #body
    #details
    write("Car under construction!", font=("Verdana", 15, "normal"))

def Boat():
    #goto(-40, 85)
    #The Boat
    #Body
    #sail
    write("Boat under construction!", font=("Verdana", 15, "normal"))


#============================================================================

# Fruits

def Banana():
    #goto(-40, 85)
    #The Banana
    #base
    #details
    write("Banana is under construction!", font=("Verdana", 15, "normal"))

    
def Grapes():
    #goto(-40, 85)
    #The Grapes
    #body
    #details
    write("Grapes are under construction!", font=("Verdana", 15, "normal"))
    
def Orange():
    #goto(-40, 85)
    #The Orange
    #body
    #details
    write("Orange is under construction!", font=("Verdana", 15, "normal"))