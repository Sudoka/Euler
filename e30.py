#!/usr/bin/python -tt
import re
import sys
from euler import *

def main():
  score = 0
  for i in xrange(10,6*9**5):
    sod = 0
    for digit in str(i):
      sod += int(digit)**5
    if sod == i: score += i
  print score
    


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
