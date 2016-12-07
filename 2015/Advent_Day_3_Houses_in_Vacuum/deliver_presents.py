#!/usr/bin/env python3

class house_points(object):
  def __init__(self,x,y):
    self.x = x
    self.y = y
  
  def __str__(self):
    return "({0},{1})".format(self.x,self.y)
  
def main():
  directions = get_input_file() 
  print(deliver_presents(directions[0].strip()))

def deliver_presents(directions):
  drop_offs = {}
  x,y   = 0,0
  rx,ry = 0,0
  sx,sy = 0,0
  drop_offs[(x,y)] = 2
  pos = 0

  for house in directions:
    if pos % 2 == 0:
      sx,sy = direction(house,sx,sy)
      x,y = sx,sy
    else:

      x,y = rx,ry
    
    if drop_offs.get((x,y)) == None:
      drop_offs[(x,y)] = 1

    pos = pos + 1

  return len(drop_offs)

def direction(house,x,y):
  if house == '<':
    x -= 1      
  elif house == '>':
    x += 1
  elif house == '^':
    y += 1
  elif house == 'v':
    y -= 1
  
  return x,y

def get_input_file():
  with open('./day_3_input.txt', 'r') as f:
    read_data = f.readlines()

  f.closed
  return read_data

main()
