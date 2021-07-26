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
border_pen.color("pink")
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
score_panel.setposition(-290, 280)
scorestring = "Score: %s" % score
score_panel.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
# score_panel.hideturtle()

# Spaceship / Player
spaceship = turtle.Turtle()
spaceship.color("blue")
spaceship.shape("triangle")
spaceship.penup()
spaceship.speed(0)
spaceship.goto(0, -250)
spaceship.left(90)  # player.setheading(90)
sapceship_speed = 20
spaceship_speed = 20
spaceship.direction = "stop"

# Invader(s)
number_of_invaders = 4
invaders = []
# Create a list of invaders of turtle
for i in range(number_of_invaders):
    invaders.append(turtle.Turtle())

for enemy in invaders:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(180, 250)
    enemy.goto(x, y)

invaders_speed = 2


# Weapon(s) / Missile
missile = turtle.Turtle()
missile.color("yellow")
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

# Movements
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
            spaceship.setx(x - spaceship_speed)

    if spaceship.direction == "right":
        if x > 270:
            x = 280
            spaceship.setx(x)

        else:
            spaceship.setx(x + spaceship_speed)

    # For Dynamic/Automatic  movement just comment this
    # spaceship.direction = 'stop'


# For Missile
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


# Keybinding
wn.listen()
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(fire_missile, "space")
# turtle.listen()
# turtle.onkey(go_left, "Left")
# turtle.onkey(go_right, "Right")
# turtle.onkey(fire_missile, "space")
#:::::::::::::::::::::::::OR::::::::::::::::::::::::::::::

# # Functions
# def move_left():
#     player.setx(player.xcor() - 20)

# def move_right():
#     player.setx(player.xcor() + 20)

# # Keybinding
# wn.listen()
# wn.onkeypress(move_left, 'a')
# wn.onkeypress(move_right, 'd')

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Main
while True:
    wn.update()

    move()

    # Invaders for loop
    for enemy in invaders:  # NOTE: enemy is a single invader
        x = enemy.xcor()
        y = enemy.ycor()
        enemy.setx(x + invaders_speed)

        # Reverse enemy's direction / Invader-window collision
        if x > 280:
            enemy.setx(280)
            # Reverse the enemy
            invaders_speed *= -1
            # Move all the invaders down
            for i in invaders:
                y = i.ycor()
                y -= 40
                i.sety(y)

        if x < -280:
            enemy.setx(-280)
            # Reverse the enemy
            invaders_speed *= -1
            # Move all the invaders down
            for i in invaders:
                y = i.ycor()
                y -= 40
                i.sety(y)

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
            scorestring = "Score: %s" % score
            score_panel.clear()
            score_panel.write(
                scorestring, False, align="left", font=("Arial", 14, "normal")
            )

        # Game Over OR invader-spaceship collision
        if enemy.distance(spaceship) < 25:
            enemy.hideturtle()
            spaceship.hideturtle()
            missile.hideturtle()
            break

    # Missile fire
    if missile_state == "fire":
        ym = missile.ycor()
        missile.sety(ym + missile_speed)

    # Missile reset (out of bounds)
    if missile.ycor() > 275:
        missile.hideturtle()
        missilestate = "ready"


delay = raw_input("Press enter to finsh.")
wn.mainloop()
