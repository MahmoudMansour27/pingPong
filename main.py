# Keep the code as clean as possible at all the time!!
# libraries
from Classes import racket
from Classes import Ball
from Classes import textWrite
from Classes import triangle
import turtle

window = turtle.Screen()  # initialize the screen
window.title("Ping Pong")  # set the screen's title
window.bgcolor("black")  # set the screen's background as black
window.setup(width=800, height=600)  # set the screen's width and height
window.tracer(0)  # stop screen auto update


def window_screen():
    window.clear()
    options = turtle.Screen()  # initialize the screen
    options.title("Ping Pong")  # set the screen's title
    options.bgcolor("black")  # set the screen's background as black
    options.setup(width=800, height=600)  # set the screen's width and height
    options.tracer(0)  # stop screen auto update


# shapes

# rackets
racket1 = racket("racket1", "square", "blue", -350, 0, 5, 1)
racket1.setObject()
racket2 = racket("racket2", "square", "red", 350, 0, 5, 1)
racket2.setObject()

# ball
ball = Ball("ball", "circle", "white", 0, 0, 1, 1)
ball.__set_Object__()
ball.dy = 0.1
ball.dx = 0.1

tri = triangle("t", 190)
tri.draw()

# text
welcome = textWrite("welcome", "white", 0, 200, "Welcome", 23, "bold")
welcome.text()
play = textWrite("play", "white", 0, 150, "play", 22, "normal")
play.text()
Exit = textWrite("Exit", "white", 0, 100, "Exit", 22, "normal")
Exit.text()

# score

# Keyboard bindings
window.listen()  # expect input key
window.onkeypress(racket1.move_up, "w")  # when w key pressed,do the function
window.onkeypress(racket1.move_down, "s")
window.onkeypress(racket2.move_up, "Up")
window.onkeypress(racket2.move_down, "Down")
window.onkeypress(tri.move_up, "q")
window.onkeypress(tri.move_down, "a")
'''
if tri.move_up() == 190 or tri.move_down() == 190:
    window.onkeypress(window_screen, "Return")
'''
# main game loop
#def game_loop():
while True:
    window.update()  # update the screen in the beginning
    if tri.move_down() or tri.move_up() == 190:
        print("play")
    # ball movement
    ball.__xy_increase__(ball.dx, ball.dy)

    # border check
    if ball.__y_cor__() > 290:
        ball.__set_y__(290)
        ball.dy *= -1
    elif ball.__y_cor__() < -290:
        ball.__set_y__(-290)
        ball.dy *= -1
    elif ball.__x_cor__() > 390:
        ball.__go_to__(0, 0)
        ball.dx *= -1
    elif ball.__x_cor__() < -390:
        ball.__go_to__(0, 0)
        ball.dx *= -1
    # reflection with rackets
    elif (ball.__x_cor__() > 340 and ball.__x_cor__() < 350) and (
            ball.__y_cor__() < racket2.__y_cor__() + 40 and ball.__y_cor__() > racket2.__y_cor__() - 40):
        ball.__set_x__(340)
        ball.dx *= -1
    elif (ball.__x_cor__() < -340 and ball.__x_cor__() > -350) and (
            ball.__y_cor__() < racket1.__y_cor__() + 40 and ball.__y_cor__() > racket1.__y_cor__() - 40):
        ball.__set_x__(-340)
        ball.dx *= -1

# scoring
