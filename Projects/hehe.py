import turtle
import random
import math

# --- Cinematic Engine Setup ---
screen = turtle.Screen()
screen.setup(1000, 700)
screen.bgcolor("#0a0500")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()

# --- Assets & Rendering ---
def draw_detailed_arthur(frame):
    # Breathing effect calculation
    breath = math.sin(frame * 0.1) * 3
    
    # 1. THE COAT & SHOULDERS (Texture layers)
    t.penup(); t.goto(-250, -350 + breath)
    t.color("#1a110a"); t.begin_fill()
    t.goto(250, -350 + breath); t.goto(180, -100 + breath)
    t.goto(-180, -100 + breath); t.end_fill()

    # 2. THE FACE (Rugged Detail)
    t.color("#4d331f"); t.penup(); t.goto(-70, -100 + breath); t.begin_fill()
    t.goto(70, -100 + breath); t.goto(60, 20 + breath); t.goto(-60, 20 + breath); t.end_fill()
    
    # Facial Shadow/Beard Grain
    t.color("#1a0f00")
    for _ in range(150):
        t.penup()
        t.goto(random.randint(-55, 55), random.randint(-100, -20) + breath)
        t.dot(random.randint(1, 3))

    # 3. THE ICONIC STETSON (High Detail)
    # Brim Bottom
    t.color("#000000"); t.penup(); t.goto(-180, -20 + breath); t.begin_fill()
    t.goto(180, -20 + breath); t.goto(160, 10 + breath); t.goto(-160, 10 + breath); t.end_fill()
    # Brim Top/Crown
    t.color("#26190d"); t.penup(); t.goto(-85, 10 + breath); t.begin_fill()
    t.goto(85, 10 + breath); t.goto(75, 120 + breath)
    # The 'Gunslinger' dent in the crown
    t.goto(0, 100 + breath); t.goto(-75, 120 + breath); t.end_fill()
    # Hat Band (Leather detail)
    t.color("#3d2b1f"); t.penup(); t.goto(-80, 25 + breath)
    t.begin_fill(); t.goto(80, 25 + breath); t.goto(82, 40 + breath); t.goto(-82, 40 + breath); t.end_fill()

def draw_environment(frame):
    # Dynamic Sunset Glow (Ray Casting Simulation)
    glow_size = 200 + math.sin(frame * 0.05) * 10
    t.penup(); t.goto(300, 150)
    for i in range(10):
        t.dot(glow_size + (i * 20), (0.2, 0.05, 0, 1 - (i * 0.1))) # Custom RGB tuples
    
    # Floating Embers (Weather System)
    for _ in range(25):
        t.penup()
        ex = random.randint(-500, 500)
        ey = random.randint(-350, 350)
        t.color(random.choice(["#ff6600", "#ffcc00", "#ffffff"]))
        t.goto(ex, ey)
        t.dot(random.randint(1, 4))

def render_loop(frame=0):
    t.clear()
    
    # Background "Red Dead" Gradient
    t.penup(); t.goto(-500, 350)
    t.color("#3d0000"); t.begin_fill()
    for _ in range(2): t.forward(1000); t.right(90); t.forward(700); t.right(90)
    t.end_fill()

    draw_environment(frame)
    draw_detailed_arthur(frame)

    # Cinematic Black Bars (Letterbox)
    t.color("black")
    t.penup(); t.goto(-500, 350); t.begin_fill()
    for _ in range(2): t.forward(1000); t.right(90); t.forward(80); t.right(90)
    t.end_fill()
    t.penup(); t.goto(-500, -270); t.begin_fill()
    for _ in range(2): t.forward(1000); t.right(90); t.forward(80); t.right(90)
    t.end_fill()

    screen.update()
    screen.ontimer(lambda: render_loop(frame + 1), 20)

# --- Boot Up ---
render_loop()
screen.exitonclick()
