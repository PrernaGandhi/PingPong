from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = True


def bye():
    global game_is_on
    game_is_on = False


# TODO 1: Create the screen
screen = Screen()
screen.title("Ping Pong")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

# TODO 2: Create and move paddle
right_paddle = Paddle((350, 0))
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

# TODO 3: Create another paddle for two player game
left_paddle = Paddle((-350, 0))
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
# TODO 4: Create the ball and make it move
# screen.tracer(1)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(bye, "x")
while game_is_on:
    # screen update need to happen in a while loop
    # we need to update it everytime
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # TODO 5: Detect collision with wall and bounce back
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    # TODO 6: Detect collision with paddle
    # collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() >= 330:
        ball.bounce_x()
        # ball.increase_ball_speed()
    # collision with left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() <= -330:
        ball.bounce_x()
        # ball.increase_ball_speed()

    # TODO 7: Detect when paddle misses the ball
    # TODO 8: Keep the score
    # right side misses
    if ball.xcor() > 400:
        ball.reset_position()
        # when right side misses, point goes to left player
        scoreboard.l_score()

    if ball.xcor() < - 400:
        ball.reset_position()
        # when left side misses, point goes to right player
        scoreboard.r_score()
# screen.exitonclick()
