import turtle
from winsound import PlaySound, SND_ASYNC

def main():
    window_height = 400
    window_width = 700

    window = create_the_window("Pong Game by rabyaeAyoub", "green", window_width, window_height, 0)
    
    # Paddle A
    paddle_a_position = -((window_width / 2) - 50)
    paddle_a = create_paddle("square", "yellow", 5, 1, paddle_a_position, 0, 0)

    # Paddle B
    paddle_b_position = -paddle_a_position
    paddle_b = create_paddle("square", "yellow", 5, 1, paddle_b_position, 0, 0)

    # Ball
    ball = create_ball("circle", "white", 0, 0, 0, 0.15, 0.15)

    # Pen
    pen_string = {
        "string": "Player A: 0 | Player B: 0",
        "align": "center",
        "font-family": "Courier",
        "font-size": 16,
        "font-style": "normal"
    }
    pen = create_pen(0, "black", 0, (window_height / 2) - 40, pen_string)

    score = {
        "a": 0,
        "b": 0
    }

    def paddle_a_up():
        paddle_up(paddle_a)

    def paddle_a_down():
        paddle_down(paddle_a)

    def paddle_b_up():
        paddle_up(paddle_b)

    def paddle_b_down():
        paddle_down(paddle_b)

    # Keyboard Binding
    window.listen()
    window.onkeypress(paddle_a_up, "w")
    window.onkeypress(paddle_a_down, "s")
    window.onkeypress(paddle_b_up, "Up")
    window.onkeypress(paddle_b_down, "Down")

    # Main game loop
    while True:
        window.update()

        # Ball Movement
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        # increase score
        increase_score(ball, pen, (window_width / 2) - 10, -((window_width / 2) - 10), pen_string, score)
        
        # Border checking
        check_up_down_borders(ball, (window_height / 2) - 10)
        check_right_left_borders(ball, (window_width / 2) - 10)

        
        # Paddle and Ball collisions
        ball_right_paddle_collision(ball, paddle_b_position, paddle_b)
        ball_left_paddle_collision(ball, paddle_a_position, paddle_a)
        

def create_the_window(title: str, color: str, width: float, height: float, tracer: int):
    window = turtle.Screen()
    window.title(title)
    window.bgcolor(color)
    window.setup(width=width, height=height)
    window.tracer(tracer)

    return window


def create_paddle(shape: str, color: str, width: float, height: float, x: float, y: float, speed: int):
    paddle = turtle.Turtle()
    paddle.speed(speed)
    paddle.shape(shape)
    paddle.color(color)
    paddle.shapesize(stretch_wid=width, stretch_len=height)
    paddle.penup()
    paddle.goto(x, y)

    return paddle


def create_ball(shape: str, color: str, x: float, y: float, speed: int, dx: float, dy: float):
    ball = turtle.Turtle()
    ball.speed(speed)
    ball.shape(shape)
    ball.color(color)
    ball.penup()
    ball.goto(x, y)
    ball.dx = dx
    ball.dy = dy

    return ball


def paddle_up(paddle):
    y = paddle.ycor() + 20
    paddle.sety(y)


def paddle_down(paddle):
    y = paddle.ycor() - 20
    paddle.sety(y)


def check_up_down_borders(ball: turtle.Turtle, height: int):
    if ball.ycor() > height:
        ball.sety(height)
        ball.dy *= -1
        PlaySound("./sounds/bounce.wav", SND_ASYNC)

    if ball.ycor() < -height:
        ball.sety(-height)
        ball.dy *= -1
        PlaySound("./sounds/bounce.wav", SND_ASYNC)


def check_right_left_borders(ball: turtle.Turtle, width: int):
    if ball.xcor() > width:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -width:
        ball.goto(0, 0)
        ball.dx *= -1


def ball_right_paddle_collision(ball: turtle.Turtle, paddle_right_position, paddle_right):
    if (ball.xcor() > paddle_right_position - 10 and ball.xcor() < paddle_right_position) and (ball.ycor() < paddle_right.ycor() + 50 and ball.ycor() > paddle_right.ycor() - 50):
        ball.setx(paddle_right_position - 10)
        ball.dx *= -1
        PlaySound("./sounds/bounce.wav", SND_ASYNC)


def ball_left_paddle_collision(ball: turtle.Turtle, paddle_left_position, paddle_left):
    if (ball.xcor() < paddle_left_position + 10 and ball.xcor() > paddle_left_position - 10) and (ball.ycor() < paddle_left.ycor() + 50 and ball.ycor() > paddle_left.ycor() - 50):
        ball.setx(paddle_left_position + 10)
        ball.dx *= -1
        PlaySound("./sounds/bounce.wav", SND_ASYNC)


def create_pen(speed: float, color: str, x: str, y: str, pen_string):
    pen = turtle.Turtle()
    pen.speed(speed)
    pen.color(color)
    pen.hideturtle()
    pen.penup()
    pen.goto(x, y)
    pen.write(pen_string["string"] , align=pen_string["align"], font=(pen_string["font-family"], pen_string["font-size"], pen_string["font-style"]))

    return pen


def increase_score(ball: turtle.Turtle, pen: turtle.Turtle, right_border: int, left_border: int, string_dict, score):
    score_a = score["a"]
    score_b = score["b"]
    if ball.xcor() > right_border:
        score["a"] += 1
        score_a = score["a"]
        pen.clear()
        pen.write(f"Player A: {score_a} | Player B: {score_b}" , align=string_dict["align"], font=(string_dict["font-family"], string_dict["font-size"], string_dict["font-style"]))
    
    if ball.xcor() < left_border:
        score["b"] += 1
        score_b = score["b"]
        pen.clear()
        pen.write(f"Player A: {score_a} | Player B: {score_b}" , align=string_dict["align"], font=(string_dict["font-family"], string_dict["font-size"], string_dict["font-style"]))


main()