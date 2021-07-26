import turtle

wn = turtle.Screen()
wn.title("Demo")
wn.bgcolor("black")
wn.setup(655, 655)
# wn.tracer(0)

tur = turtle.Turtle()
tur.shape('turtle')
tur.color('red')
tur.goto(0, 0)
tur.pendown()


i = 0
def move():
    global i
    i += 1
    tur.fd(1)
    tur.lt(1)

while 1:
    # wn.update()
    move()