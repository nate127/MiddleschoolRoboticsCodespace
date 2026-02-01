import turtle, time, random
from utils import *

# Section 1 - setup
# TODO - set a background using set_background()
set_background("noFilter")
# TODO - create at least "two variables and set their starting value. ex: cookies = 0
mangos = 0
optiplex = 1
cost = 50
# OPTIONAL: use this invisible alien to say a message
message_sprite = create_sprite("alien", -300,200)
message_sprite.hideturtle()



# Section 2 - controls
# TODO - define an action. ex: def my_control()
def get_optiplex():
    global mangos, optiplex, cost
    if mangos >= cost:
        cost = cost * 2
        optiplex += 1
        x = -400 + 120 * optiplex
        y = -250
        create_sprite("image", x, y)
def get_mangos():
    global mangos
    mangos += 2
window.onkeypress(get_mangos,"space")
window.onkeypress(get_optiplex,"o")
mangos += optiplex
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control





# Section 3 - game loop
window.listen()
for i in range(1000000000):
    message_sprite.color("blue")
    message_sprite.clear()
    message_sprite.write(f"mangos: {mangos}\nCost: {cost}\noptiplex: {optiplex}", font=("arial",15,"bold"))

    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("MINE MY MANGO COIN FORVER OR ELSE")

    time.sleep(0.01)
    window.update()