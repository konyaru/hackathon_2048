import tkinter as tk
import math
import random
import itertools
from time import sleep

root = None
canvas = None
tiles = []

SQUARE_LENGTH = 100
RADIUS = SQUARE_LENGTH / 2 - 5
POSITION = {"x": 8, "y": 8}
BORDER_WIDTH = 8
SIZE = 4
LENGTH = SQUARE_LENGTH * SIZE + BORDER_WIDTH * SIZE
CELL_COLOR = '#cbbeb5'
BORDER_COLOR = '#b2a698'

# fieldを作成→描画系
def set_field():
  canvas.create_rectangle(POSITION["x"], POSITION["y"], LENGTH + POSITION["x"], LENGTH + POSITION["y"], fill='#cbbeb5', width=BORDER_WIDTH, outline=BORDER_COLOR)

  for i in range(SIZE - 1):
    x = POSITION["x"] + SQUARE_LENGTH * (i + 1) + BORDER_WIDTH * i + BORDER_WIDTH
    y = POSITION["y"] + SQUARE_LENGTH * (i + 1) + BORDER_WIDTH * i + BORDER_WIDTH
    canvas.create_line(x, POSITION["y"], x, LENGTH + POSITION["y"], width=BORDER_WIDTH, fill=BORDER_COLOR)
    canvas.create_line(POSITION["x"], y, LENGTH + POSITION["x"], y, width=BORDER_WIDTH, fill=BORDER_COLOR)

# 描画系
def create_canvas():
  root = tk.Tk()
  root.geometry(f"""{LENGTH + POSITION["x"] * 2}x{LENGTH + POSITION["y"] * 2}""")
  root.title("2048")
  canvas = tk.Canvas(root, width=(LENGTH + POSITION["x"]), height=(LENGTH + POSITION["y"]))
  canvas.place(x=0, y=0)

  return root, canvas

# 番号を描画
def set_number(num, x, y):
  center_x = POSITION["x"] + BORDER_WIDTH * x + BORDER_WIDTH / 2 + SQUARE_LENGTH * x + SQUARE_LENGTH / 2
  center_y = POSITION["y"] + BORDER_WIDTH * y + BORDER_WIDTH / 2 + SQUARE_LENGTH * y + SQUARE_LENGTH / 2
  canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill=CELL_COLOR, width=0)
  canvas.create_text(center_x, center_y, text=num, justify="center", font=("", 70), tag="count_text")

def draw_tiles():
  for column in range(len(tiles)):
    for row in range(len(tiles[column])):
      set_number(tiles[column][row].value, row, column)

def move_tiles(key_input):
  global tiles
  if key_input == 'Left':
    for line in tiles:
      calc(line)
  if key_input == 'Right':
    for line in tiles:
      copy_line = line.copy()
      copy_line.reverse()
      calc(copy_line)
  if key_input == 'Up':
    for i in range(SIZE):
      tmp_line = []
      for j in range(SIZE):
        tmp_line.append(tiles[j][i])
      calc(tmp_line)
  if key_input == 'Down':
    for i in range(SIZE):
      tmp_line = []
      for j in range(SIZE):
        tmp_line.append(tiles[j][i])
      copy_line = tmp_line.copy()
      copy_line.reverse()
      calc(copy_line)
  
  tiles.

  
  draw_tiles()
    

def calc(line):
    for i in range(len(line) - 1):
      for j in range((i + 1), len(line)):
        if line[j].value != 0:
          if line[i].value == 0:
            line[i].value = line[j].value
            line[j].value = 0
          elif line[i].value == line[j].value:
            (line[i].value, line[j].value) = (line[i].value*2, 0)
          else:
            break
            
              
            

# 操作系
def operate(event):
  print(event.keysym)
  key_input = event.keysym
  move_tiles(key_input)

def reset():
  process()

class Tile:
  def __init__(self):
    self.value = 0

  def set_random_value(self):
    self.value = random.choice([2, 4])

# ここからプログラム書く
class Game:
  def __init__(self):
    self.tiles = self.create_tiles()

  def create_tiles(self):
    tiles =  [[Tile() for row in range(SIZE)] for column in range(SIZE)]
    self.set_init_value(tiles)
    return tiles

  def set_init_value(self, tiles):
    random_tiles = random.sample(list(itertools.chain.from_iterable(tiles)), 2)
    for tile in random_tiles:
      tile.set_random_value()

def initialize():
  global root, canvas
  root, canvas = create_canvas()
  set_field()

def process():
  global tiles
  game = Game()
  tiles = game.tiles
  for i, v in enumerate([0, 2, 4, 2]):
    tiles[0][i].value = v
  for i, v in enumerate([0, 2, 2, 2]):
    tiles[1][i].value = v
  for i, v in enumerate([0, 4, 2, 2]):
    tiles[2][i].value = v
  for i, v in enumerate([2, 2, 2, 2]):
    tiles[3][i].value = v
  draw_tiles()
  # set_number("2", 0, 2)
  # set_number("4", 2, 1)
  root.bind("<Key>", lambda event: operate(event))
  root.bind("<Control-Return>", lambda event: reset())
  root.mainloop()

def play():
  initialize()
  process()

play()
