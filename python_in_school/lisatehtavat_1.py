from math import sqrt


def distance():
    # File lisatehtavat_1, Tehtava 1
    # Ask for user input for the x,y values
    x1 = int(input("Enter x1: "))

    y1 = int(input("Enter y1: "))

    x2 = int(input("Enter x2: "))

    y2 = int(input("Enter y2: "))

    # Calculate the distance between the two points
    distance = sqrt((x2-x1)**2 + (y2-y1)**2)

    # Output the distance
    print(distance)



# Celsius to fahrenheit converter
def celsius_to_fahrenheit():
    celsius = int(input("Enter °C: ")) # User input celsius
    fahrenheit = celsius * 1.8 + 32 # Calculate fahrenheit
    print(f"{celsius}°C is {fahrenheit}°F") # Output the result



def print_humans():

    head = " 0 "
    body = "-+-"
    legs = "/ \\"

    user_input = int(input("How many people do you want to see? \nEnter amount: " ))
    if user_input > 15: # Validate that user input is 15 or less
        print("Don't overcrowd the planet!")
        return


#    def print_body(part):  # Print the user defined amount of humans
#        for x in range(user_input):
#            if x != user_input - 1:
#                print(part, end=" ")
#            else:
#                print(part)

    def print_body(part):  # Print the user defined amount of humans
        for x in range(user_input):
                print(part, end=" ")
        print()

    print_body(head)
    print_body(body)
    print_body(legs)


    # Select which one to execute
def which():
    selection = input("Which one do you want to activate?\nType calc to open the point to point calculator\nType temp to open the celsius to fahrenheit converter\nType people to print x amount of people\nChoose: ").lower()
    if selection == "calc":
        distance()
    elif selection == "temp":
        celsius_to_fahrenheit()
    elif selection == "people":
        print_humans()
    else:
        print("Not a valid option")
        return

which()