import turtle


class racket:
    def __init__(self, name, shape, color, Xposition, Yposition, stretch_wid, stretch_len):
        self.name = name
        self.shape = shape
        self.color = color
        self.Xposition = Xposition
        self.Yposition = Yposition
        self.stretch_wid = stretch_wid
        self.stretch_len = stretch_len

    def setObject(self):
        self.name = turtle.Turtle()
        self.name.speed(0)  # set the speed of the animation (0 is the greatest)
        self.name.shape(self.shape)  # set the shape of the object
        self.name.color(self.color)  # set the color of the object
        self.name.shapesize(self.stretch_wid, self.stretch_len)  # stretches the shape
        self.name.penup()  # stops the object drawing lines
        self.name.goto(self.Xposition, self.Yposition)  # set the positions of the object

    def move_up(self):
        y = self.name.ycor()  # get y coordinate
        y += 20  # increase y coordinate by 20
        self.name.sety(y)  # set new y coordinate

    def move_down(self):
        y = self.name.ycor()
        y -= 20
        self.name.sety(y)

    def __y_cor__(self):
        return self.name.ycor()

    def __x_cor__(self):
        return self.name.xcor()


class Ball:
    def __init__(self, name, shape, color, Xposition, Yposition, stretch_wid, stretch_len):
        self.name = name
        self.shape = shape
        self.color = color
        self.Xposition = Xposition
        self.Yposition = Yposition
        self.stretch_wid = stretch_wid
        self.stretch_len = stretch_len

    def __set_Object__(self):
        self.name = turtle.Turtle()
        self.name.speed(0)  # set the speed of the animation (0 is the greatest)
        self.name.shape(self.shape)  # set the shape of the object
        self.name.color(self.color)  # set the color of the object
        self.name.shapesize(self.stretch_wid, self.stretch_len)  # stretches the shape
        self.name.penup()  # stops the object drawing lines
        self.name.goto(self.Xposition, self.Yposition)  # set the positions of the object

    def __xy_increase__(self, x, y):
        self.name.setx(self.name.xcor() + x)  # X coordinate increased
        self.name.sety(self.name.ycor() + y)  # Y coordinate increased

    def __y_cor__(self):
        return self.name.ycor()

    def __x_cor__(self):
        return self.name.xcor()

    def __set_y__(self, y):
        self.name.sety(y)

    def __set_x__(self, x):
        self.name.setx(x)

    def __go_to__(self, x, y):
        self.name.goto(x, y)


class textWrite:
    def __init__(self, name, color, x_position, y_position, message, font_size, font_weight):
        self.message = message
        self.name = name
        self.color = color
        self.x_position = x_position
        self.y_position = y_position
        self.font_size = font_size
        self.font_weight = font_weight

    def text(self):
        self.name = turtle.Turtle()
        self.name.speed(0)
        self.name.color(self.color)
        self.name.penup()
        self.name.hideturtle()
        self.name.goto(self.x_position, self.y_position)
        self.name.write(self.message, align="center", font=("Courier", self.font_size, self.font_weight))


class triangle:
    def __init__(self, name, start_position):
        self.name = name
        self.start_position = start_position
        self.name = turtle.Turtle()

    def draw(self):
        self.name.speed(0)
        self.name.color("blue")
        self.name.hideturtle()
        self.name.penup()
        self.name.goto(-80, self.start_position)
        self.name.pendown()
        self.name.forward(150)
        self.name.right(90)
        self.name.forward(40)
        self.name.right(90)
        self.name.forward(150)
        self.name.right(90)
        self.name.forward(40)
        y_position = self.name.ycor()
        return y_position

    def move_up(self):
        if self.move_down() == 140:
            y = 140
        self.name.goto(-80, (y+50))
        self.name.clear()
        self.name.right(90)
        self.name.forward(150)
        self.name.right(90)
        self.name.forward(40)
        self.name.right(90)
        self.name.forward(150)
        self.name.right(90)
        self.name.forward(40)
        return self.name.ycor()

    def move_down(self):
        self.name.goto(-80, (self.start_position-50))
        self.name.clear()
        self.name.right(90)
        self.name.forward(150)
        self.name.right(90)
        self.name.forward(40)
        self.name.right(90)
        self.name.forward(150)
        self.name.right(90)
        self.name.forward(40)
        return self.name.ycor()
