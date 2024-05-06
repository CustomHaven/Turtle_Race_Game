import random
from turtle import Turtle

class Player:
  """Buleprint for the player."""
  def __init__(self, turtle_shape, x_start, y_start, color, width, height) -> None:
    self.turtle = Turtle(turtle_shape)
    self.x = x_start
    self.y = y_start
    self.color = color
    self.screen_width = width
    self.screen_height = height
    self.turtle_height = 20
    self.turtle_width = 20
    self.turtle_size = self.turtle_height + self.turtle_width

  def get_color(self):
    """Return the player's colours."""
    return self.turtle.pencolor()

  def start_race(self) -> None:
    """Starting race positions."""
    self.turtle.speed("slowest")
    self.turtle.color((self.color))
    self.turtle.penup()
    self.turtle.goto(self.x, self.y)
    self.turtle.showturtle()
  
  def forward(self) -> None:
    """Moves the player forward."""
    self.turtle.fd(random.randint(1, 10))
    x_coords = self.turtle.xcor()
    self.x = x_coords
  
  def finish_line(self):
    """Checks if player has reached finishing line."""
    return self.x > (self.screen_width/2) - (self.turtle_size / 2)