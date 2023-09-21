import turtle
#Turtle settings
turtle.shape("turtle")
turtle.fillcolor("green")
turtle. speed(100)

#Animals
def Panda():
    #The Panda
    turtle.goto(0,0)
    turtle.pendown()
    turtle.color("Black")
    turtle.circle(200)
    turtle.penup()
    #ears
    turtle.goto(-200,250)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("Black")
    turtle.circle(100)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(200,250)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("Black")
    turtle.circle(100)
    turtle.end_fill()
    turtle.penup()
    #nose
    turtle.goto(0,100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("Black")
    turtle.circle(30)
    turtle.end_fill()
    turtle.penup()

    #cheeks
    turtle.goto(-100,130)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("pink")
    turtle.circle(45)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(100,130)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("pink")
    turtle.circle(45)
    turtle.end_fill()
    turtle.penup()
    #eyes
    turtle.goto(-88,155)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("Black")
    turtle.circle(45)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(88,155)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("Black")
    turtle.circle(45)
    turtle.end_fill()
    turtle.penup()
    #big eye highlights
    turtle.goto(-80,189)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("white")
    turtle.circle(24)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(80,189)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("White")
    turtle.circle(24)
    turtle.end_fill()
    turtle.penup()
    #small eye highlights
    turtle.goto(-100,163)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("White")
    turtle.circle(15)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(100,163)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("White")
    turtle.circle(15)
    turtle.end_fill()
    turtle.penup()
    #mouth
    turtle.goto(-83,100)
    turtle.pensize(7)
    turtle.pendown()
    turtle.color("Black")
    turtle.right(90)
    turtle.circle(40, 180)
    turtle.penup()

    turtle.goto(0,100)
    turtle.pendown()
    turtle.color("Black")
    turtle.left(180)
    turtle.circle(40, 180)
    turtle.penup()

    
def Cat():
        #The Cat
    turtle.goto(0,0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#242526")
    turtle.circle(200)
    turtle.end_fill()
    turtle.penup()

    #ears
    turtle.goto(-190,240)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#242526")
    turtle.goto(-250,400)
    turtle.goto(-90,340)
    turtle.goto(-190,240)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(190,240)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#242526")
    turtle.goto(250,400)
    turtle.goto(90,340)
    turtle.goto(190,240)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(-190,260)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#FCBACB")
    turtle.goto(-220,370)
    turtle.goto(-119,345)
    turtle.goto(-190,260)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(190,260)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#FCBACB")
    turtle.goto(220,370)
    turtle.goto(119,345)
    turtle.goto(190,260)
    turtle.end_fill()
    turtle.penup()

    #eyes
    turtle.goto(-100,150)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("Black")
    turtle.circle(45)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(100,150)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("Black")
    turtle.circle(45)
    turtle.end_fill()
    turtle.penup()

    #big eye highlights
    turtle.goto(-105,190)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("white")
    turtle.circle(24)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(105,190)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("White")
    turtle.circle(24)
    turtle.end_fill()
    turtle.penup()

    #small eye highlights
    turtle.goto(-100,153)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("White")
    turtle.circle(15)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(100,153)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("White")
    turtle.circle(15)
    turtle.end_fill()
    turtle.penup()

    #nose
    turtle.goto(45,150)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#FCBACB")
    turtle.goto(45,150)
    turtle.goto(-45,150)
    turtle.goto(0,100)
    turtle.end_fill()
    turtle.penup()

    #mouth
    turtle.goto(-83,100)
    turtle.pensize(7)
    turtle.pendown()
    turtle.color("Black")
    turtle.right(90)
    turtle.circle(40, 180)
    turtle.penup()

    turtle.goto(0,100)
    turtle.pendown()
    turtle.color("Black")
    turtle.left(180)
    turtle.circle(40, 180)
    turtle.penup()
    
    
def Sheep():
    #The Sheep

    #legs
    turtle.penup()
    turtle.goto(250,25)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("black")
    turtle.goto(250,25)
    turtle.goto(250,-50)
    turtle.goto(275,-50)
    turtle.goto(275,25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(125,25)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.goto(125,25)
    turtle.goto(125,-50)
    turtle.goto(150,-50)
    turtle.goto(150,25)
    turtle.end_fill()
    turtle.penup()

    #body
    turtle.penup()
    turtle.goto(275,100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(250,100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(210,105)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(170,100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(130,105)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(90,90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()
    #break
    turtle.penup()
    turtle.goto(80,70)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(120,70)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(160,70)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(200,70)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(240,70)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(275,70)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()
    #break

    turtle.penup()
    turtle.goto(250,50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(210,50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(170,50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(125,50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(80,50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(275,50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()
    #break

    turtle.penup()
    turtle.goto(275,30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(90,30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(125,30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(170,30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(210,30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(250,30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(275,30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()
    #break

    turtle.penup()
    turtle.goto(125,15)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(170,15)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(210,15)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(220,15)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(250,15)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    turtle.penup()
    turtle.goto(275,15)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#d3d3d3")
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()

    #head
    turtle.penup()
    turtle.goto(300,30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("black")
    turtle.circle(50)
    turtle.end_fill()
    turtle.penup()

    #eyes
    turtle.goto(275,70)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("white")
    turtle.circle(15)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(325,70)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("white")
    turtle.circle(15)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(275,80)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("black")
    turtle.circle(8)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(325,80)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("black")
    turtle.circle(8)
    turtle.end_fill()
    turtle.penup()
    
#Vehicles
    
def Truck():
    #The Truck
    turtle.goto(-40, 85)
    #wheels
    #body
    #details
    
def Car():
    #The Car
    turtle.goto(-40, 85)
    #Wheels
    #body
    #details
    
def Boat():
    turtle.goto(-40, 85)
    #The Boat
    #Body
    #sail
    
#Fruits
    
def Banana():
    turtle.goto(-40, 85)
    #The Banana
    #base
    #details
    
def Grapes():
    turtle.goto(-40, 85)
    #The Grapes
    #body
    #details
    
def Orange():
    turtle.goto(-40, 85)
    #The Orange
    #body
    #details
    
#Ask user which theme to draw
answer=input("Hello! I am drawing software. I have three themes you can chose from: animals, vehicles or fruits. Please pick one of the above. ")

#If anwer is animal
if answer=="animal":
    print("Great choice!" )
    answer=input("Now pick one of these 3 animals: panda, cat or sheep. ")
    if answer=="panda":
        Panda()
    elif answer=="cat":
        Cat()
    else:
        Sheep()
#If answer is vehicle
elif answer=="vehicle":
    print ("Sorry to inform: this feature isn't avaible yet")
    answer=input
    if answer=="car":
        Car()
    elif answer=="truck":
        Truck()
    else:
        answer=="boat"
        Boat()
#If answer is fruit
else:
    print ("Sorry to inform: this feature isn't avaible yet")
    answer=input
    if answer=="banana":
        Banana()
    elif answer=="orange":
        Orange()
    else:
        answer=="grapes"
        Grapes()


turtle.done()