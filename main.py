import turtle
import pandas
from state_naming import StateName
screen = turtle.Screen()
screen.title("US. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

game_on = True
while game_on:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name")

    if len(data[data["state"] == answer_state]) == 1:
        selected_state = data[data.state == answer_state]
        coor_x = int(selected_state.x)
        coor_y = int(selected_state.y)
        print(selected_state)
        write_state = StateName(coor_x, coor_y, answer_state)

screen.exitonclick()