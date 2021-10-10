import time
from turtle import Screen, Turtle
from random import choice

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Breakout")
screen.tracer(0)
screen.colormode(255)

# ------------------------ Paddle -------------------#

paddle = Turtle()
paddle.shape("square")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.color("white")
paddle.up()
paddle.goto(0, -250)


def go_left():
    new_x = paddle.xcor() - 15
    paddle.goto(new_x, paddle.ycor())


def go_right():
    new_x = paddle.xcor() + 15
    paddle.goto(new_x, paddle.ycor())


# ------------------------ Ball -------------------#

ball = Turtle()
ball.shape("circle")
ball.color("white")
ball.up()
ball.x_speed = 7
ball.y_speed = 7


def move():
    new_x = ball.xcor() + ball.x_speed
    new_y = ball.ycor() + ball.y_speed
    ball.goto(new_x, new_y)


# ------------------------ Bricks -------------------#

color_list = [(249, 212, 93), (150, 69, 97), (53, 99, 155), (232, 137, 62), (107, 174, 211), (243, 237, 241),
              (114, 83, 59), (201, 146, 177), (200, 77, 109), (145, 134, 72), (230, 90, 59), (141, 192, 140),
              (72, 103, 90), (68, 162, 92), (5, 165, 179), (227, 161, 183), (115, 126, 142), (163, 196, 221),
              (16, 66, 123), (187, 24, 34), (13, 56, 103), (235, 172, 160), (175, 201, 179), (163, 200, 215),
              (186, 27, 25), (80, 55, 37), (96, 61, 30)]


class Brick(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color(choice(color_list))
        self.up()
        self.goto(position)

    def vanish(self):
        self.ht()
        del self


position_list = [(-325, 275), (-200, 275), (-75, 275), (50, 275), (175, 275), (300, 275),
                 (-325, 235), (-200, 235), (-75, 235), (50, 235), (175, 235), (300, 235),
                 (-325, 195), (-200, 195), (-75, 195), (50, 195), (175, 195), (300, 195)]

# ------------------------ Gameplay -------------------#

brick_list = []
bricks_left = 18

for position in position_list:
    brick_list.append(Brick(position))

screen.listen()
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

game_on = True
while game_on:
    time.sleep(0.02)
    screen.update()
    move()

    # Collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.y_speed *= -1
    if ball.xcor() > 385 or ball.xcor() < -385:
        ball.x_speed *= -1

    # Collision with paddle
    if ball.distance(paddle) < 50:
        ball.y_speed *= -1

    # Game Over
    game_over = Turtle()
    game_over.hideturtle()

    if ball.ycor() < -280:
        screen.title("Game Over")

        game_over.showturtle()
        game_over.color("white")
        game_over.write("Game Over", font=("Times New Roman", 50, "normal"), align="center")

        game_on = False

    # Collision with brick

    for brick in brick_list:
        if ball.distance(brick) < 50:
            brick.goto(1000, 1000)
            brick.ht()
            bricks_left -= 1
            del brick
            print(bricks_left)
            ball.y_speed *= -1

    # You Won! #
    you_won = Turtle()
    you_won.hideturtle()
    you_won.color("green")

    if bricks_left == 0:
        you_won.showturtle()
        you_won.write("You Won!", font=("Times New Roman", 50, "normal"), align="center")

        game_on = False

screen.exitonclick()
