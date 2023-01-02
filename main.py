import turtle
import pandas

image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)

turtle.shape(image)

text = turtle.Turtle()
text.hideturtle()
text.penup()


data = pandas.read_csv("50_states.csv")

STATE = data["state"]
X = data["x"]
Y = data["y"]

states_guessed = []

game_on = True

while game_on:
    score = len(states_guessed)
    answer_state = screen.textinput(title=f"{score}/50 states guessed", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        states_list = []
        for item in data["state"]:
            if item not in states_guessed:
                states_list.append(item)

        df = pandas.DataFrame(states_list)
        df.to_csv("states_to_learn.csv")

        break

    for state in data["state"]:
        if answer_state == state:
            x = int(data[data.state == state].x)
            y = int(data[data.state == state].y)
            text.goto(x, y)
            text.write(arg=answer_state)
            states_guessed.append(state)
            if score == 50:
                game_on = False
                text.write(arg="YOU WIN!")



# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

turtle.exitonclick()
