from turtle import Turtle, Screen

sc = Screen()
sc.setup(height=600, width=600)
sc.bgcolor("black")
sc.title("My Snake Game")
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)














sc.exitonclick()
