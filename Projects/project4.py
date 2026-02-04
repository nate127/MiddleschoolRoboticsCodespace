import turtle, time, random
from utils import *
turtle.setup(width=964, height=540)
# Section 1 - setup
# TODO - set a background using set_background()
set_background("backk")
# TODO - create at least "two variables and set their starting value. ex: cookies = 0
mangos = 0
optiplex = 0
cost = 50
gpu = 0
gpu_cost = 2000
# OPTIONAL: use this invisible alien to say a message
message_sprite = create_sprite("alien", -435,140)
message_sprite.hideturtle()



# Section 2 - controls
# TODO - define an action. ex: def my_control()
def get_gpu():
    global mangos, gpu, gpu_cost
    if mangos >= gpu_cost:
        mangos -= gpu_cost
        gpu_cost = gpu_cost * 1.5
        gpu += 1
        x = -400 + 120 * gpu
        y = 250
        create_sprite("gpu1", x, y)
def get_optiplex():
    global mangos, optiplex, cost
    if mangos >= cost:
        mangos -= cost
        cost = cost * 2
        optiplex += 1
        x = -400 + 120 * optiplex
        y = -200
        create_sprite("image", x, y)
def get_mangos():
    global mangos
    mangos += 2
window.onkeypress(get_mangos,"space")
window.onkeypress(get_optiplex,"o")
window.onkeypress(get_gpu,"g")
mangos += optiplex
mangos += gpu * 50
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control





# Section 3 - game loop
window.listen()
for i in range(1000000000):
    message_sprite.color("red")
    message_sprite.clear()
    message_sprite.write(f"money: {mangos}\nCost: {cost}\noptiplex: {optiplex}\n gpu: {gpu}\ngpu_cost: {gpu_cost}", font=("",15,"bold"))

    # TODO - put any automatic actions here
    mangos += optiplex
    mangos += gpu * 50
    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("MINE MY MANGO COIN FORVER OR ELSE")

    time.sleep(0.1)
    window.update()