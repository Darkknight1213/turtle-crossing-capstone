import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
turtle.register_shape("f.gif")


class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("f.gif")
        self.color("red")
        self.penup()
        self.move_distance = 10
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.fd(self.move_distance)

    def go_d(self):
        self.bk(self.move_distance)

    def return_home(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def inc_speed(self):
        self.move_distance += 1



