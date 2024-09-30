import time
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard

#######setup screen############
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


#############Setup Snake#########
'''lets create three turtles
which are shaped like squares 
the squares are besides each oter
and are white in color
'''

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")




'''Move the Snake'''
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with wall
    if abs(snake.head.xcor()) >= 300 or abs(snake.head.ycor()) >= 300:
        game_on = False
        scoreboard.game_over()

    #detect collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()


    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        #extend snake length
        snake.extend()


#when we click screen exits
screen.exitonclick()