import turtle
import random
import time

delay = 0.1
sc = 0
hs = 0
bodies = []

# Creating a screen
s = turtle.Screen()
s.title("SNAKE")
s.bgcolor("blue")
s.setup(width=600, height=600)

# Creating the body of the snake
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("light blue")
head.fillcolor("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Creating a food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.fillcolor("red")
food.penup()
food.ht()
food.goto(150, 200)
food.st()

# Creating a scoreboard
sb = turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-250, 250)
sb.write("Score:0  |  Highest Score:0")

# Creating functions
def moveUp():
    if head.direction != "down":
        head.direction = "up"

def moveDown():
    if head.direction != "up":
        head.direction = "down"

def moveLeft():
    if head.direction != "right":
        head.direction = "left"

def moveRight():
    if head.direction != "left":
        head.direction = "right"

def moveStop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Event handling
s.listen()
s.onkey(moveUp, "Up")
s.onkey(moveDown, "Down")
s.onkey(moveLeft, "Left")
s.onkey(moveRight, "Right")
s.onkey(moveStop, "space")

# Main Loop
while True:
    s.update()
    # Check collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        # Hide bodies
        for body in bodies:
            body.ht()
        bodies.clear()
        sc = 0
        delay = 0.1
        sb.clear()
        sb.write("Score:{}  |  Highest Score:{}".format(sc, hs))

    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        # Increase the body of the snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)

        sc = sc + 10
        delay = delay - 0.001
        if sc > hs:
            hs = sc
        sb.clear()
        sb.write("Score:{}  |  Highest Score:{}".format(sc, hs))

    # Move snake bodies
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with bodies
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # Hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()
            sc = 0
            delay = 0.1
            sb.clear()
            sb.write("Score:{}  |  Highest Score:{}".format(sc, hs))

    time.sleep(delay)

s.mainloop()
