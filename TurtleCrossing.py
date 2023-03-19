from data import *
from turtle import *
a, b = Cross(), Screen()
a.screen()
a.starting_position()
a.writing_turtle()
b.onkey(a.up,"w")
a.lines()
a.make_cars()
while True:
    a.turtle()
    a.cars_moving()
    if a.cars_disapeard():
        a.center_cars()
    if a.crossed():
        a.win()
        break
    elif a.hit_car():
        a.game_over()
        break
    
a.holdscreen()