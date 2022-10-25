class Goomba:
  def __init__(self):
    self.goomba_num = 2
    self.is_moving = True
    self.lives = 1
    self.color = "brown"

class Block: 
  def __init__(self):
    self.produce_coin = 1
    self.block_num = 3
    self.unit_size = 1
    self.texture = "brick"

class Pipe:
  def __init__(self):
    self.usable = True
    self.height = 2
    self.color = "green"
    self.start_position = True


  