#!/usr/bin/env python3

def main():
  instructions = get_input_file()
  for instruction in instructions:
    instruction = instruction.strip()
    signal, wire = instruction.split('->')

def get_input_file():
  with open('./day_7_input.txt', 'r') as f:
    read_data = f.readlines()

  f.closed
  return read_data

main()
