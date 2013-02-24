#!/usr/bin/python -tt
import re
import sys
from euler import *

def main():
  nums = [3, 7]
  dens = [2, 5]
  target = 0
  while len(nums) < 1000:
    nums.append(2*nums[-1]+nums[-2])
    dens.append(2*dens[-1]+dens[-2])
    if len(str(nums[-1])) > len(str(dens[-1])):
      target += 1
  print target

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
