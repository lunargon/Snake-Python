from turtle import Screen, Turtle

# start posistions of snake
START_POS = [(0, 0), (-20, 0), (-40, 0)]

# Distance when move
MOVE_DIS = 20

# angle for moving
UP = 90
DOWN = -90
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.seg_ls = []
        self.create_snake()
        self.head = self.seg_ls[0]

    def create_snake(self):
        # Create Snake
        for pos in START_POS:
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(pos)
            self.seg_ls.append(segment)

    def move(self):
        for seg in range(len(self.seg_ls) - 1, 0, -1):
            new_x = self.seg_ls[seg - 1].xcor()
            new_y = self.seg_ls[seg - 1].ycor()
            self.seg_ls[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)