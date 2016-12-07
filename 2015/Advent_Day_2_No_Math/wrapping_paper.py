#!/usr/bin/env python

def main():
  ptot = 0
  rtot = 0
  for size in get_input_file():
    p,r = cal_prism(size.strip())
    ptot = ptot + p
    rtot = rtot + r

  print("Total wrapping {0}".format(ptot))
  print("Total ribbon   {0}".format(rtot))

def cal_prism(dimensions):
  sides = sorted(list(map(int, dimensions.split('x'))))

  ribbon = cal_ribbon(sides[0],sides[1],sides[2])
  prism = 2*sides[0]*sides[1] + 2*sides[0]*sides[2] + 2*sides[1]*sides[2] + (sides[0]*sides[1]) 

  return prism, ribbon
def cal_ribbon(w,l,h):
  return w+w+l+l+(w*l*h)
  
def get_input_file():
  with open('./day_2_input.txt', 'r') as f:
    read_data = f.readlines()

  f.closed
  return read_data

main()
