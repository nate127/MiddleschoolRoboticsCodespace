# Section 1 - Your code
from utils import *
set_background("New Project (1)")

s1 = create_sprite("rock_climbers", 100, 100)
s2 = create_sprite("dog", -100, 100)
s3 = create_sprite("cardinal", -100, -100)
s4 = create_sprite("New Project", 100, -100)
s5 = create_sprite("New Project (2)", 0, 0)
message1 = create_sprite("alien",-200,200)
message1.color("red")
message1.write("nate",font = ("", 20, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-200,-250)
message2.color("black")
message2.write("Nate means gift of god",font = ("Arial", 20, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()