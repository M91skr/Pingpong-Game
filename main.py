"""---------------------------------------- Pingpong Game ----------------------------------------
This project is a **Pingpong Game**.
In this game, two users can play ping pong together with a common keyboard.
One user uses the up and down arrow keys and the other user uses the q and a keys to move the racket vertically.
"""

# ---------------------------------------- Add Required Library ----------------------------------------

import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

# ---------------------------------------- Play Space Creation ----------------------------------------

screen = Screen()
screen.bgcolor("green")
screen.title("Pong Game")
screen.setup(800, 600)
screen.tracer(0)

# ---------------------------------------- Adding Paddles, ball and Scoreboard into the Game Space --------------------

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

# ---------------------------------------- Define the Function of Arrow Keys ----------------------------------------

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "q")
screen.onkey(l_paddle.go_down, "a")

# ---------------------------------------- Game Running ----------------------------------------

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # ---------------------------------------- The Ball From Leaving the Length of The Table Prevention ---------------

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    if r_paddle.ycor() > 300:
        r_paddle.bounce_down()
    elif l_paddle.ycor() > 300:
        l_paddle.bounce_down()
    elif r_paddle.ycor() < -300:
        r_paddle.bounce_up()
    elif l_paddle.ycor() < -300:
        l_paddle.bounce_up()

    # ---------------------------------------- The Ball From Leaving the Width of The Table Prevention ---------------

    if ball.distance(r_paddle) < 58 and ball.xcor() > 320 or ball.distance(l_paddle) < 58 and ball.xcor() < -320:
        ball.bounce_x()

    # ---------------------------------------- Success Definition ----------------------------------------

    elif ball.xcor() > 380:
        ball.reset_position()
        score.update_l_score()

    elif ball.xcor() < -380:
        ball.reset_position()
        score.update_r_score()

screen.exitonclick()
