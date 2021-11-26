import turtle
import time
import random

delay = 0.1
segments = []
score = 0
high_score = 0

# Screen set up
canvas = turtle.Screen()
canvas.title("My Snake Game")
canvas.setup(width=600, height=600)
canvas.bgcolor("orange")
canvas.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("turtle")
head.color("green")

head.penup()
head.goto(0, 100)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")

food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)

# create pen to write score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "bold"))


# Movement function
def move() :
    if head.direction == "up" :
        y = head.ycor() # y coordinate of the turtle
        head.sety(y + 20)

    if head.direction == "down" :
        y = head.ycor() # y coordinate of the turtle
        head.sety(y - 20)

    if head.direction == "right" :
        x = head.xcor() # x coordinate of the turtle
        head.setx(x + 20)

    if head.direction == "left" :
        x = head.xcor() # x coordinate of the turtle
        head.setx(x - 20)

# Direction function
def go_up():
    if head.direction != "down":
        head.direction = "up"
 
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
 
def go_left():
    if head.direction != "right":
        head.direction = "left"


# Main game loop
while True :
    canvas.update()
    
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        score = 0

        for segment in segment :
            segment.goto(1000, 1000)
        segments.clear()

    if head.distance(food) < 15:
        # move the food to a random position on screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        score += 10

        if score > high_score :
            high_score = score

        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("turtle")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

    # move the end segment in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)


    move()

    for segment in segments :
        if segment.distance(head) < 20 :
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])

            for segment in segments :
                segment.goto(1000,1000)
            segment.clear()

    # Keyboard input

    canvas.listen()
    canvas.onkey(go_up, "w")
    canvas.onkey(go_down, "s")
    canvas.onkey(go_right, "d")
    canvas.onkey(go_left, "a")
    time.sleep(delay)

    # Scoreboard
    pen.clear()
    pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "bold"))