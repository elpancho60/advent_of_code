#!/usr/bin/env python3


def main():
  words = get_input_file()
  total_nice = 0
  total_new_nice = 0


  for w in words:
    w = w.strip()
    if is_nice(w):
      total_nice += 1
    if is_new_nice(w):
      total_new_nice += 1

  print("Total number of nice words {0}".format(total_nice))
  print("Total number of new nice words {0}".format(total_new_nice))

def is_nice(word):
  return has_3_vowels(word) and has_2_in_row(word) and not_have_strings(word)

def has_3_vowels(w):
  if w.count('a') + w.count('e') + w.count('i') + w.count('o') + w.count('u') >= 3:
    return True

def has_2_in_row(w):
  return [ True for i in range(len(w)-1) if w[i] == w[i+1] ]

def not_have_strings(w):
  nono = [ 'ab', 'cd', 'pq', 'xy' ]
  for n in nono:
    if n in w:  
      return False 

  return True

def is_new_nice(word):
  return contains_pair(word) and does_it_repeat(word)
  
def contains_pair(w):
  for i in range(len(w)-2):
    p = w[i] + w[i+1]
    if p in w[i+2:]:
      return True  

def does_it_repeat(w):
  for i in range(len(w)-2):
    if w[i] == w[i+2]:
      return True
  
def get_input_file():
  with open('./day_5_input.txt', 'r') as f:
    read_data = f.readlines()

  f.closed
  return read_data


main()
