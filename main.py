import random
from turtle import Screen
from player import Player

screen = Screen()
w = 500
h = 400
screen.setup(width=w, height=h)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
count = 0
turtles = []
game_on = True

for starting_y in range(-150, 151, 50):
  new_turtles = Player("turtle", -230, starting_y, colors[count], w, h)
  new_turtles.start_race()
  turtles.append(new_turtles)
  count += 1

while game_on:
  pick_random_turtles = [random.choice(turtles) for _ in range(random.randint(0, 6))]
  for turtle in pick_random_turtles:
    turtle.forward()
    if turtle.finish_line():
      if turtle.get_color() == user_bet:
        print(f"You've won! The {turtle.get_color()} turtle is the winner!")
      else:
        print(f"You've lost! The {turtle.get_color()} turtle is the winner!")
      game_on = False
      break

screen.exitonclick()