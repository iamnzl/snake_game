from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.write(f"Score : {self.score}", font=('Arial', 15, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", font=('Arial', 15, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",font=('Arial', 15, 'normal'))
