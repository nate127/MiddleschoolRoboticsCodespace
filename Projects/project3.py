import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 =-200
y1 =150
x2 =-200
y2 =0
x3 =-200
y3 =-100
x4 =-200
y4 =-200


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("finish line")
t1 = create_sprite("fish",x1,y1)
t2 = create_sprite("bike",x2,y2)
t3 = create_sprite("basketball",x3,y3)
t4 = create_sprite("dog",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# the fish is most likely to win due to it having the largest minimum speed. the basketball has the highest top speed, but a larger variation of speeds
for i in range(45):
    x1 +=random.randint(9,16)
    x2 +=random.randint(0,10)
    x3 +=random.randint(0,20)
    x4 +=random.randint(9,11)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("fish wins!")
if x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("bike wins!")
if x3 >= x2 and x3 >= x1 and x1 >= x4:
    print("basketball wins!")
if x4 >= x2 and x4 >= x3 and x4 >= x1:
    print("dog wins!")
turtle.exitonclick()