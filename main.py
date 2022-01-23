import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_d, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with player
    for car in car_manager.all_cars:
        if car.distance(player) < 35:
            score.score = 1
            score.update_scoreboard()
            player.return_home()
            car_manager.car_speed = 5

    # detect finishing line
    if player.is_at_finish_line():
        player.return_home()
        car_manager.level_up()
        player.inc_speed()
        score.inc_score()

screen.mainloop()

