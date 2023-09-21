import turtle
import time

turtle.shape(name='turtle')
turtle.color('green')

def turtle_run():
    time.sleep(2)
    turtle.forward(100)
    turtle.right(90)
    print(f"running round {x}")

x = 1
rounds = int(input("How many rounds: "))

for x in range(rounds):
    turtle_run()
    x = x + 1
    

turtle.done()