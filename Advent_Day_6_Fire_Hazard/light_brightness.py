#!/usr/bin/env python3

GRID_SIZE=1000

def main():
  xmas_lights = {} 
  instructions = get_input_file()
  for i in instructions:
    xmas_lights = step_thru(i, xmas_lights)

  print(sum([val for val in xmas_lights.values() if val]))

def get_input_file():
  with open('day_6_input.txt', 'r') as f:
    read_data = f.readlines()

  f.closed

  return read_data

def step_thru(instructions,xmas_lights):
  todo, start, stop = parse_inst(instructions)

  startx,starty = getXY(start)
  stopx,stopy   = getXY(stop)

  for x in range(startx,stopx+1):
    for y in range(starty,stopy+1):
      bright = xmas_lights.get((x,y),0)

      if todo == 'off' and bright > 0:
        xmas_lights[(x,y)] = bright - 1
      elif todo == 'on':
        xmas_lights[(x,y)] = bright + 1
      elif todo == 'toggle':
        xmas_lights[(x,y)] = bright + 2

  return xmas_lights

def getXY(pair):
  x,y = pair.split(',')
  return int(x), int(y)

def parse_inst(i):
  parts = i.split()
  t = parts[0] if parts[0] == "toggle" else parts[1] 
     
  return t, parts[-3], parts[-1]

main()
