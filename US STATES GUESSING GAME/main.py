import turtle
import pandas

score = 0

screen = turtle.Screen()
screen.title("US STATES GUESSING GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
remaining = []

while len(guessed_states) <= 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 STATES CORRECT", "").title()

    if answer_state == "Exit":
        state_data = data[data.state == answer_state]
        for states in all_states:
            if states not in guessed_states:
                remaining.append(states)
        new_data = pandas.DataFrame(remaining)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)

