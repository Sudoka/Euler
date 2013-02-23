#!/usr/bin/python -tt
import re
import sys
from euler import *

def main():
  nums = [2, 3, 8]
  i = 4
  while len(nums) < 100:
    nums.append(nums[-1]+nums[-2])
    nums.append(nums[-1]+nums[-2])
    nums.append(i*nums[-1]+nums[-2])
    i += 2
  print sum([int(ch) for ch in str(nums[99])])

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
