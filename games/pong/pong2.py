from turtle import Turtle, Screen
from winsound import PlaySound, SND_ASYNC

def main():
    colors = {
        "window": "green",
        "paddles": "yellow",
        "ball": "white",
        "text": "black"
    }
    window_size = {
        "width": 800,
        "height": 550
    }

    # Create the window the window
    window = create_the_window("Pong Game by rabyaeAyoub", colors["window"], window_size["width"], window_size["height"], 0)

    # Paddles
    paddles_parms = {
        "speed": 0, #check this line
        "color": colors["paddles"],
        "y": 0,
        "width": 6,
        "height": 1,
        "shape": "square",
        "dy": 20
    }
    x_paddle = window_size["width"]/2-50

    paddle_a = create_paddle(**paddles_parms, x=-x_paddle)

    paddle_b = create_paddle(**paddles_parms, x=x_paddle)

    # Ball
    ball_params = {
        "speed": 0,
        "color": colors["ball"],
        "x": 0,
        "y": 0,
        "shape": "circle",
        "width": 1.2,
        "height": 1.2,
        "dx": 0.2,
        "dy": 0.2
    }
    max_height_to_ball = window_size["height"] / 2 - (((ball_params["width"] / ball_params["height"]) * 20) / 2 + 5)
    max_width_to_ball = window_size["width"] / 2 - (((ball_params["height"] / ball_params["width"]) * 20) / 2 + 5)
    ball = create_ball(**ball_params)

    # Pen (Show Results)
    score = {
        "a": 0,
        "b": 0,
    }
    pen_parms = {
        "result_text": "Player A: 0 | Player B: 0",
        "align": "center",
        "font": ("Courier", 15, "normal"),
        "color": "black",
        "y": (window_size["height"] / 2) - 40
    }
    # (text: str, align: str, font: tuple[str, int, str], color: str, x: float, y: float) -> Turtle
    pen = create_pen(**pen_parms)

    # Paddles Functionality
    max_height_to_paddles = window_size["height"] / 2 - (((paddles_parms["width"] / paddles_parms["height"]) * 20) / 2 + 5)

    def paddle_a_up():
        paddle_up(paddle_a, max_height_to_paddles)

    def paddle_a_down():
        paddle_down(paddle_a, -max_height_to_paddles)

    def paddle_b_up():
        paddle_up(paddle_b, max_height_to_paddles)

    def paddle_b_down():
        paddle_down(paddle_b, -max_height_to_paddles)


    # The main loop of the game
    while True:
        window.update()

        # Check borders
        check_up_down_borders(ball, max_height_to_ball)
        check_right_left_borders(ball, max_width_to_ball)

        # Ball movement
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        # Observe window
        window.listen()
        window.onkeypress(fun=paddle_a_up, key="w")
        window.onkeypress(fun=paddle_a_down, key="s")
        window.onkeypress(fun=paddle_b_up, key="Up")
        window.onkeypress(fun=paddle_b_down, key="Down")

        # Increase score
        increase_score(ball, pen, pen_parms, score, max_width_to_ball)

        # Check colosions
        check_right_paddle_collosion(ball, paddle_b, ball_params["height"] * 20, paddles_parms["width"] * 20)
        check_left_paddle_collosion(ball, paddle_a, ball_params["height"] * 20, paddles_parms["width"] * 20)


def create_the_window(title: str, bg: str, width: float, height: float, tracer: float):
    window = Screen()
    window.title(title)
    window.bgcolor(bg)
    window.setup(width, height)
    window.tracer(tracer) # check this line
    
    return window


def create_paddle(speed: float, color: str, x: float, y: float, shape: str, width: float, height: float, dy: float):
    paddle = Turtle()
    paddle.speed(speed)
    paddle.color(color)
    paddle.penup()
    paddle.goto(x, y)
    paddle.shape(shape)
    paddle.shapesize(stretch_wid=width, stretch_len=height)
    paddle.dy = dy

    return paddle


def create_ball(speed: float, color: str, x: float, y: float, shape: str, width: float, height: float, dy: float, dx: float):
    ball = Turtle()
    ball.speed(speed)
    ball.color(color)
    ball.shape(shape)
    ball.shapesize(width, height)
    ball.penup()
    ball.goto(x, y)
    ball.dy = dy
    ball.dx = dx

    return ball


def paddle_up(paddle: Turtle, max_height: float):
    if paddle.ycor() >= max_height:
        paddle.sety(max_height)
    else:
        paddle.sety(paddle.ycor() + paddle.dy)


def paddle_down(paddle: Turtle, min_height: float):
    if paddle.ycor() <= min_height:
        paddle.sety(min_height)
    else:
        paddle.sety(paddle.ycor() - paddle.dy)


def check_up_down_borders(ball: Turtle, max_height: float):
    if ball.ycor() >= max_height:
        ball.sety(max_height)
        ball.dy *= -1
        PlaySound("./sounds/bounce.wav", SND_ASYNC)
    elif ball.ycor() <= -max_height:
        ball.sety(-max_height)
        ball.dy *= -1
        PlaySound("./sounds/bounce.wav", SND_ASYNC)


def check_right_left_borders(ball: Turtle, max_width: float):
    if ball.xcor() >= max_width:
        ball.goto(0, 0)
        ball.dx *= -1
    elif ball.xcor() <= -max_width:
        ball.goto(0, 0)
        ball.dx *= -1


def check_right_paddle_collosion(ball: Turtle, paddle: Turtle, ball_width: float, paddle_height):
    if (ball.xcor() + ball_width - (ball_width / 2) > paddle.xcor() and ball.xcor() < paddle.xcor()) and ((ball.ycor() < paddle.ycor() + (paddle_height / 2)) and (ball.ycor() > paddle.ycor() - (paddle_height / 2))):
        ball.dx *= -1
        PlaySound("./sounds/bounce.wav", SND_ASYNC)


def check_left_paddle_collosion(ball: Turtle, paddle: Turtle, ball_width: float, paddle_height):
    if (ball.xcor() - ball_width + (ball_width / 2) < paddle.xcor() and ball.xcor() > paddle.xcor()) and ((ball.ycor() < paddle.ycor() + (paddle_height / 2)) and (ball.ycor() > paddle.ycor() - (paddle_height / 2))):
        ball.dx *= -1
        PlaySound("./sounds/bounce.wav", SND_ASYNC)


def create_pen(result_text: str, align: str, font: tuple[str, int, str], color: str, y: float):
    pen = Turtle()
    pen.penup()
    pen.sety(y)
    pen.hideturtle()
    pen.write(result_text, align=align, font=font)
    pen.color(color)

    return pen


def increase_score(ball: Turtle, pen: Turtle, pen_params: dict, score: dict[str, int], max_width: float):
    if ball.xcor() >= max_width:
        score["a"] += 1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score["a"], score["b"]), align=pen_params["align"], font=pen_params["font"])
        PlaySound("./sounds/Plink.wav", SND_ASYNC)
    elif ball.xcor() <= -max_width:
        score["b"] += 1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score["a"], score["b"]), align=pen_params["align"], font=pen_params["font"])
        PlaySound("./sounds/Plink.wav", SND_ASYNC)


main()