import turtle
import shapes

#Turtle settings
turtle.shape("turtle")
turtle.fillcolor("green")
turtle.speed(100)

# Select the topic of animation
topic = input("Which topic do you want to animate? A for Animals, V for Vehicles or F for Fruits, select one: ").lower()


if topic == "a":
    animal = input("You have selected animals as the topic, now which animal would you like to animate? P for Panda, C for Cat or S for Sheep, select one: ").lower()
    if animal == "p":
        shapes.Panda()
    elif animal == "c":
        shapes.Cat()
    elif animal == "s":
        shapes.Sheep()
    else:
        print("Invalid option")
        quit()
elif topic == "v":
    vehicle = input("You have selected vehicles as the topic, now which vehicle would you like to animate? T for Truck, C for Car or B for Boat, select one: ").lower()
    if vehicle == "t":
        shapes.Truck()
    elif vehicle == "c":
        shapes.Car()
    elif vehicle == "b":
        shapes.Boat()
    else:
        print("Invalid option")
        quit()
elif topic == "f":
    fruit = input("You have selected fruits as the topic, now which fruit would you like to animate? B for Banana, G for Grapes or O for Orange, select one: ").lower()
    if fruit == "b":
        shapes.Banana()
    elif fruit == "g":
        shapes.Grapes()
    elif fruit == "o":
        shapes.Orange()
    else:
        print("Invalid option")
        quit()
else:
    print("Invalid option")
    quit()

turtle.exitonclick()
