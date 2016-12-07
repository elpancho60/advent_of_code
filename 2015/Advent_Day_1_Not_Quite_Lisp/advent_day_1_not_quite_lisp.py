#!/usr/bin/env python

def main():
  input_data = get_input_file()
  floor, position = what_floor(input_data)

  print("Floor: {0}".format(floor))
  print("Position: {0}".format(position))

#def get_input_url():
#  url = 'http://adventofcode.com/day/1/input'
#
#  buffer = BytesIO()
#  c = pycurl.Curl()
#  c.setopt(c.URL, url) 
#  c.setopt(c.WRITEDATA, buffer)
#  c.perform()
#  c.close()
#  
#  body = buffer.getvalue()
#  # Body is a byte string.
#  # We have to know the encoding in order to print it to a text file
#  # such as standard output.
#  print(body.decode('iso-8859-1'))

def get_input_file():
  with open('day_1_input.txt', 'r') as f:
    read_data = f.read()

  f.closed

  return read_data

def what_floor(data):
  floor = 0
  s = 1
  basement = None
  for pos in data:
    if pos == '(':
      floor += 1
    elif pos == ')':
      floor -= 1
    else:
      continue

    if floor == -1 and basement == None:
      basement = s

    s += 1

  return(floor,basement)

main()
