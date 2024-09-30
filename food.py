import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        """Inherit food from turtle class"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.2, 0.2, 1)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


