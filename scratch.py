from turtle import Turtle, Screen

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
turtle = Turtle()
turtle.color("white")
turtle.hideturtle()
turtle.penup()
turtle.goto(0,280)
turtle.write("yo", align="left")




screen.exitonclick()
