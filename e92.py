#!/usr/bin/python -tt
import re
import sys
from euler import *
from time import time

def main():

  #see if a chain of next_nums ends up at 89. use memoization and voila
  ones = set()
  ones.add(1)
  ens = set()
  ens.add(89)
  for i in xrange(1, 10000000):
    nums = []
    n = i
    nums.append(n)
    while not n in ens and not n in ones:
      n = next_num(n)
      nums.append(n)
    if n in ens:
      for num in nums:
        ens.add(num)
    elif n in ones:
      for num in nums:
        ones.add(num)


  print len(ens)
    
    

# given a number n, sum up and square each of the digits
def next_num(n):
  s = str(n)
  nextnum = 0
  for digit in s: nextnum += int(digit)**2
  return nextnum


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
