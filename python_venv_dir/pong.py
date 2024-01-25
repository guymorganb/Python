from graphics import *


def main():
    win_width = 800
    win_height = 600
    paddle_width = 10
    paddle_height = 80
    ball_radius = 10
    paddle_speed = 15
    ball_speed_x = 2
    ball_speed_y = 2
    game_running = False

    # Create the game window
    win = GraphWin("Pong", win_width, win_height)
    win.setBackground("black")

    # Create the paddles
    left_paddle = Rectangle(Point(10, win_height / 2 - paddle_height / 2),
                            Point(10 + paddle_width, win_height / 2 + paddle_height / 2))
    left_paddle.setFill("white")
    left_paddle.draw(win)

    right_paddle = Rectangle(Point(win_width - 10 - paddle_width, win_height / 2 - paddle_height / 2),
                             Point(win_width - 10, win_height / 2 + paddle_height / 2))
    right_paddle.setFill("white")
    right_paddle.draw(win)

    # Create the ball
    ball = Circle(Point(win_width / 2, win_height / 2), ball_radius)
    ball.setFill("white")
    ball.draw(win)

    # Create the start button
    start_button = Rectangle(Point(win_width / 2 - 30, win_height / 2 - 20),
                             Point(win_width / 2 + 30, win_height / 2 + 20))
    start_button.setFill("green")
    start_button_label = Text(start_button.getCenter(), "Start")
    start_button_label.setTextColor("white")
    start_button.draw(win)
    start_button_label.draw(win)

    # Create the pause button
    pause_button = Rectangle(Point(win_width / 2 - 30, win_height / 2 + 40),
                             Point(win_width / 2 + 30, win_height / 2 + 80))
    pause_button.setFill("red")
    pause_button_label = Text(pause_button.getCenter(), "Pause")
    pause_button_label.setTextColor("white")
    pause_button.draw(win)
    pause_button_label.draw(win)

    # Move the paddles
    def move_paddle(paddle, direction):
        paddle.move(0, paddle_speed * direction)

        # Prevent paddles from moving outside the window
        if paddle.getCenter().getY() - paddle_height / 2 <= 0:
            paddle.move(0, paddle_speed)
        elif paddle.getCenter().getY() + paddle_height / 2 >= win_height:
            paddle.move(0, -paddle_speed)

    # Move the ball
    def move_ball():
        nonlocal ball_speed_x, ball_speed_y

        ball.move(ball_speed_x, ball_speed_y)

        ball_center = ball.getCenter()
        if ball_center.getY() - ball_radius <= 0 or ball_center.getY() + ball_radius >= win_height:
            # Reverse ball's vertical direction if it hits the top or bottom wall
            ball_speed_y *= -1

        if ball_center.getX() - ball_radius <= paddle_width and \
                left_paddle.getCenter().getY() - paddle_height / 2 <= ball_center.getY() <= \
                left_paddle.getCenter().getY() + paddle_height / 2:
            # Reverse ball's horizontal direction if it hits the left paddle
            ball_speed_x *= -1
        if ball_center.getX() + ball_radius >= win_width - paddle_width and \
                right_paddle.getCenter().getY() - paddle_height / 2 <= ball_center.getY() <= \
                right_paddle.getCenter().getY() + paddle_height / 2:
            # Reverse ball's horizontal direction if it hits the right paddle
            ball_speed_x *= -1

    # Game loop
    while True:
        key = win.checkKey()
        click = win.checkMouse()

        if key == "w":
            move_paddle(left_paddle, -1)
        elif key == "s":
            move_paddle(left_paddle, 1)
        elif key == "Up":
            move_paddle(right_paddle, -1)
        elif key == "Down":
            move_paddle(right_paddle, 1)
        elif click and start_button.getP1().getX() <= click.getX() <= start_button.getP2().getX() \
                and start_button.getP1().getY() <= click.getY() <= start_button.getP2().getY():
            # Start the game if the Start button is clicked
            game_running = True
            start_button.undraw()
            start_button_label.undraw()
        elif click and pause_button.getP1().getX() <= click.getX() <= pause_button.getP2().getX() \
                and pause_button.getP1().getY() <= click.getY() <= pause_button.getP2().getY():
            if game_running:
                # Pause the game if the Pause button is clicked
                game_running = False
            else:
                # Resume the game if the Pause button is clicked
                game_running = True

        if game_running:
            move_ball()

        update(60)

    win.close()


main()
