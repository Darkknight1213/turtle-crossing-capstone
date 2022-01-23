import random
import turtle

# cars shapes
turtle.register_shape("bus.gif")
turtle.register_shape("car.gif")
turtle.register_shape("old.gif")
turtle.register_shape("garbage-truck.gif")
turtle.register_shape("he.gif")
turtle.register_shape("helicopter.gif")
turtle.register_shape("helicopter3.gif")
turtle.register_shape("hell.gif")
turtle.register_shape("motorcycle.gif")
turtle.register_shape("sport.gif")
vehichles = ["bus.gif",
             "car.gif",
             "old.gif",
             "sport.gif",
             "garbage-truck.gif",
             "he.gif",
             "helicopter.gif",
             "helicopter3.gif",
             "hell.gif",
             "motorcycle.gif",
             "sport.gif"
             ]

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        rand_chance = random.randint(1, 6)
        if rand_chance == 1:
            new_car = turtle.Turtle()
            new_car.shape(random.choice(vehichles))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.bk(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
