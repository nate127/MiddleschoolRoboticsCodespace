import turtle, math, time, random
from utils import *
turtle.setup(width=964, height=540)
# Section 1: Setup
# TODO - create your player character and any other sprites
message_sprite = create_sprite("alien", -435,140)
message_sprite.hideturtle()
# TODO - set your background
# TODO - set the starting value for your variables
x1 = -200
y1 = -50
x2 = 200
y2 = -50
xa1 = -200
ya1 = -50
xa2 = 200
ya2 = -50
arrow1_list = []
arrow2_list = []

evil_lives = 10
good_lives = 5
sprite_list = []
set_background("grass")
s1 = create_sprite("stick1",x1,y1)
s2 = create_sprite("stick2",x2,y2)
def s1_move_up():
    global xa1, ya1, xa2, ya2
    x1 = s1.xcor()
    y1 = s1.ycor() + 15
    ya1 += 15
    s1.goto(x1,y1)
        
def s1_move_down():
    global xa1, ya1, xa2, ya2
    x1 = s1.xcor()
    y1 = s1.ycor() - 15
    ya1 += -15
    s1.goto(x1,y1)
    
def s1_move_left():
    global xa1, ya1, xa2, ya2
    x1 = s1.xcor() - 15
    y1 = s1.ycor() 
    xa1 += -15
    s1.goto(x1,y1)
    
def s1_move_right(): 
    global xa1, ya1, xa2, ya2
    x1 = s1.xcor() + 15
    y1 = s1.ycor() 
    xa1 += 15
    s1.goto(x1,y1)
    
# Section 2: Controls
# TODO - define your controls
window.onkeypress(s1_move_up, "w")
window.onkeypress(s1_move_down, "s")
window.onkeypress(s1_move_right, "d")
window.onkeypress(s1_move_left, "a")
# Section 2: Controls
# TODO - define your controls
def s2_move_up():
    global xa1, ya1, xa2, ya2
    x2 = s2.xcor()
    y2 = s2.ycor() + 15
    ya2 += 15
    s2.goto(x2,y2)
        
def s2_move_down():
    global xa1, ya1, xa2, ya2
    x2 = s2.xcor()
    y2 = s2.ycor() - 15
    ya2 += -15
    s2.goto(x2,y2)
    
def s2_move_left():
    global xa1, ya1, xa2, ya2
    x2 = s2.xcor() - 15
    y2 = s2.ycor() 
    xa2 += -15
    s2.goto(x2,y2)
    
def s2_move_right(): 
    global xa1, ya1, xa2, ya2
    x2 = s2.xcor() + 15
    y2 = s2.ycor() 
    xa2 += 15
    s2.goto(x2,y2)
    
# Section 2: Controls
def s1shoot():
    global xa1, ya1, evil_lives
    t1 = create_sprite("arrow1", xa1, ya1)
    arrow1_list.append(t1)
    for i in range(100):
        xa1 += 10
        t1.goto(xa1, ya1)
        window.update()
        time.sleep(0.01)
        if get_distance(s2, t1) < 50:
            evil_lives += -1
            break
    arrow1_list.pop()
    t1.hideturtle()
    xa1 += -1000
def s2shoot():
    global xa2,ya2,good_lives
    t2 = create_sprite("arrow2", xa2, ya2)
    arrow2_list.append(t2)
    for i in range(100):
        xa2 += -10
        t2.goto(xa2, ya2)
        window.update()
        time.sleep(0.01)
        if get_distance(s1, t2) < 50:
            good_lives += -1
            break
    arrow2_list.pop()
    t2.hideturtle()
    xa2 += 1000

# TODO - define your controls
window.onkeypress(s2_move_up, "i")
window.onkeypress(s2_move_down, "k")
window.onkeypress(s2_move_right, "l")
window.onkeypress(s2_move_left, "j")
window.onkeypress(s1shoot, "q")
window.onkeypress(s2shoot, "o")
# TODO - pick keys for each control
# Section 3: Game Loop
message_sprite.color("white")



# TODO - add code for automatic actions
window.listen()
for i in range(10000000):
    time.sleep(0.01)
    window.update()
    if evil_lives < 1:
        w1 = create_sprite("win1",0,0)
        time.sleep(5)
        window.update
        quit()
    if good_lives < 1:
        w2 = create_sprite("Player 3 wins",0,0)
        time.sleep(5)
        window.update
        quit()
    message_sprite.clear()
    message_sprite.write(f"P1 Health: {evil_lives}\nP2 Health: {good_lives}", font=("Arial",15))