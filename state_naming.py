from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class StateName(Turtle):

    def __init__(self, coor_x, coor_y, state_name):
        super().__init__()
        self.hideturtle()
        self.coor_x = coor_x
        self.coor_y = coor_y
        self.state_name = state_name
        self.penup()
        self.show_name()

    def show_name(self):
        self.goto(self.coor_x, self.coor_y)
        self.write(f"{self.state_name}", False, align=ALIGNMENT, font=FONT)
