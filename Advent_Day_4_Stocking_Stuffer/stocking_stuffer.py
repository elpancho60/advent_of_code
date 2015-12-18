#!/usr/bin/env python3

import hashlib

def main ():
  print(find_adventcoins())

def find_adventcoins():
  found = False 
  index = 0
  secert_key = 'iwrupvqb'
  #secert_key = "abcdef"

  while not found: 
    m = hashlib.md5()
    convert = secert_key + str(index)
    m.update(convert.encode('utf-8'))
    md5 = m.hexdigest()
    
    if md5.startswith('00000'):
      found = True
      break

    index += 1

  return index
main()
