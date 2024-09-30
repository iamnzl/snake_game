from turtle import Turtle

square_distance = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):

        self.segment = []


        for i in square_distance:
            self.add_segment(i)

        self.head = self.segment[0]





    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)



    def extend(self):
        self.add_segment(self.segment[-1].position())




    def move(self):
        """Move the Snake"""
        for i in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[i - 1].xcor()
            new_y = self.segment[i - 1].ycor()
            self.segment[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Head 90 degrees"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Head 270 degrees"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Head 90 degrees"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Head 90 degrees"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


