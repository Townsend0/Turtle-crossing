from turtle import *
from time import *
from random import *

max_x, max_y = 350, 250
space = 20 

class Cross:
    def __init__(self):
        self.a = [Turtle("turtle"),Turtle()]
        self.b = Screen()
        self.c = []
        self.d = []

    def screen(self):
        self.b.listen()
        self.b.colormode(255)
        self.b.title("turtle cross".title())
        self.b.bgcolor("grey")
        self.b.setup(700,500)
        self.b.tracer(0)

    def lines(self):
        s = 50
        for a in range(10):
            self.c.append(Turtle())
            self.c[a].width(4)
            self.c[a].color("white")
            self.c[a].penup()
            self.c[a].hideturtle()
            self.c[a].setheading(0)
            self.c[a].goto(-max_x,-max_y+s)
            s += 45
            while self.c[a].xcor() < max_x:
                self.c[a].pendown()
                self.c[a].forward(space)
                self.c[a].penup()
                self.c[a].forward(space)

    def holdscreen(self):
        self.b.exitonclick()

    def up(self):
        self.a[0].forward(10)

    def turtle(self):
        self.a[0].color("black")
        self.a[0].setheading(90)
        self.b.update()
        sleep(0.05)

    def starting_position(self):
        self.a[0].penup()
        self.a[0].setposition(0,-230)

    def make_cars(self):
        s = 72
        for a in range(18):
            self.d.append(Turtle("square"))
            self.d[a].color(randint(0,255),randint(0,255),randint(0,255))
            self.d[a].shapesize(1,3)
            self.d[a].penup()
            self.d[a].goto(randint(-max_x,max_x), s - max_y)
            if a%2:
                s += 45

    def cars_moving(self):
        for a in self.d:
            a.forward(randint(5,10))

    def center_cars(self):
        for a in self.d:
            if a.xcor() > space + max_x:
                a.goto(-max_x - space ,a.ycor())
                a.color(randint(0,255),randint(0,255),randint(0,255))

    def cars_disapeard(self):
        for a in self.d:
            if a.xcor() > max_x + space:
                return True
    
    def hit_car(self):
        for a in self.d:
            if ( self.a[0].distance(a) <=40 ) and ( a.ycor() - self.a[0].ycor() in range(0,23) or  self.a[0].ycor() - a.ycor() in range(0,23) ):
                return True

    def game_over(self):
        self.a[1].write("GAME OVER",False,"center",("courier",20,"normal"))


    def crossed(self):
        if self.a[0].ycor() >= 240:
            return True
        else:
            return False

    def writing_turtle(self):
        self.a[1].penup()
        self.a[1].hideturtle()
        self.a[1].color("black")
        self.a[1].goto(0,-20)
    
    def win(self):
        self.a[1].write("VICTORY!",False,"center",("courier",20,"normal"))