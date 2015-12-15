#!/usr/bin/env python

def main():
  tot = 0
  for size in get_input_file():
    tot = tot + cal_prism(size.strip())
  print(tot)

def cal_prism(dimensions):
  sides = sorted(list(map(int, dimensions.split('x'))))

  return 2*sides[0]*sides[1] + 2*sides[0]*sides[2] + 2*sides[1]*sides[2] + (sides[0]*sides[1]) 

def get_input_file():
  with open('./day_2_input.txt', 'r') as f:
    read_data = f.readlines()

  f.closed
  return read_data

main()
