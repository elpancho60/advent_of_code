#!/usr/bin/env python3

import hashlib

def main ():
  five_zeros, six_zeros = find_adventcoins()
  print("5 zeros {0}".format(five_zeros))
  print("6 zeros {0}".format(six_zeros))


def find_adventcoins():
  found = False 
  index = 0
  five = None
  six  = None
  secert_key = 'iwrupvqb'
  #secert_key = "abcdef"

  while not found: 
    m = hashlib.md5()
    convert = secert_key + str(index)
    m.update(convert.encode('utf-8'))
    md5 = m.hexdigest()
    
    if md5.startswith('00000') and five is None:
      five = index

    if md5.startswith('000000'):
      six = index

    if five is not None and six is not None:
      break

    index += 1

  return five, six 
main()
