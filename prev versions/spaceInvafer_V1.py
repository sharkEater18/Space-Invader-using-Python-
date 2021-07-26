# Those who came before me
# Lived through their vocations
# From the past until completion
# They'll turn away no ....

# Importing Libraries
import turtle
from os import *
import random
import time

delay = 0.1

# Window/ Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invader V_12.08")
wn.setup(655, 655)
wn.bgpic("bg3.gif")


# Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("#eb34e2")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pensize(3)
border_pen.down()

for side in range(4):
    border_pen.fd(600)
    border_pen.left(90)
border_pen.hideturtle()


# Scoring
score = 0
score_panel = turtle.Turtle()
score_panel.speed(0)
score_panel.color("white")
score_panel.penup()
score_panel.setposition(-290, 275)
scorestring = "Score: {}".format(score)
score_panel.write(scorestring, False, align="left", font=("Cascadia Code", 14, "bold"))
score_panel.pendown()
score_panel.hideturtle()


# Register Shapes
wn.register_shape('invd2.gif')
wn.register_shape('invd1.gif')


# Spaceship / Player
spaceship = turtle.Turtle()
spaceship.color("blue")
# spaceship.shape("triangle")
spaceship.shape("invd1.gif")
spaceship.penup()
spaceship.speed(0)
spaceship.goto(0, -250)
spaceship.left(90)  # spaceship.setheading(90)
sapceship_speed = 20
spaceship.direction = "stop"


# Invader(s)
number_of_invaders = 4
invaders = []
# Create a list of invaders of turtle
for i in range(number_of_invaders):
    invaders.append(turtle.Turtle())


for enemy in invaders:
    enemy.color("red")
    # enemy.shape("circle")
    enemy.shape("invd2.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(180, 250)
    enemy.goto(x, y)

invaders_speed = 2


# Weapon(s) / Missile
missile = turtle.Turtle()
missile.color("#de004a")
missile.shape("triangle")
missile.penup()
missile.speed(0)
missile.left(90)
missile.shapesize(0.5, 0.5)
missile.hideturtle()
# missile.goto(-150, 250)  // For testing purpose only
missile_speed = 40

# Missile State
# ready - ready to fire
# fire - on firing
missile_state = "ready"


# Functions
'''
Movements
'''
def go_left():
    spaceship.direction = "left"


def go_right():
    spaceship.direction = "right"


def move():
    x = spaceship.xcor()

    if spaceship.direction == "left":
        if x < -270:
            x = -280
            spaceship.setx(x)

        else:
            spaceship.setx(x - sapceship_speed)

    if spaceship.direction == "right":
        if x > 270:
            x = 280
            spaceship.setx(x)

        else:
            spaceship.setx(x + sapceship_speed)

    # For Dynamic/Automatic  movement just comment this
    # spaceship.direction = 'stop'

'''
For Missile
'''
def fire_missile():
    # Decalring missile state as a global
    global missile_state

    # Missile border check
    if missile.ycor() > 270:
        missile_state = "ready"

    if missile_state == "ready":
        missile_state = "fire"
        # Move the missile to just above the player
        x = spaceship.xcor()
        y = spaceship.ycor()
        missile.setx(x)
        missile.sety(y + 10)  # missile.setpos(x, y + 10)
        missile.showturtle()

def missile_main():
    # Missile fire
    if missile_state == "fire":
        ym = missile.ycor()
        missile.sety(ym + missile_speed)

    # Missile reset (out of bounds)
    if missile.ycor() > 275:
        missile.hideturtle()
        missilestate = "ready"

# Keybinding
wn.listen()
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(fire_missile, "space")


# Game Loop
game_over = False
while not game_over:
    wn.update()
    
    move()

    missile_main()

    # Invaders motion loop
    for enemy in invaders:  # NOTE: enemy is a single invader
        enemy.setx(enemy.xcor() + invaders_speed)

        # Reverse enemy's direction / Invader-window collision
        if enemy.xcor() > 280:
            enemy.setx(275)
            # Reverse the enemy
            invaders_speed *= -1
            # Move all the invaders down
            for i in invaders:
                y = i.ycor()
                y -= 40
                i.sety(y)

        if enemy.xcor() < -280:
            enemy.setx(-275)
            # Reverse the enemy
            invaders_speed *= -1
            # Move all the invaders down
            for i in invaders:
                y = i.ycor()
                y -= 40
                i.sety(y)

        
        # Game Over OR invader-spaceship collision
        if enemy.distance(spaceship) < 25:
            enemy.hideturtle()
            spaceship.hideturtle()
            missile.hideturtle()
            game_over = True
            break

        # Missile-Invader Collision Detection
        if missile.distance(enemy) < 20:
            x = random.randint(-250, 250)
            y = random.randint(180, 250)
            # enemy.goto(x, y)
            missile.hideturtle()
            missile_state = "ready"
            missile.goto(0, -500)
            enemy.setposition(x, y)
            # Increment the score
            score += 10
            scorestring = "Score: {}".format(score)
            score_panel.clear()
            score_panel.write(
                scorestring, False, align="left", font=("Cascadia Code", 14, "bold")
            )