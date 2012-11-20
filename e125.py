#!/usr/bin/python -tt
import re
import sys
from euler import *
from time import time
def main():
  max_num = 10**8
  n = max_n(max_num)
  nums = set()
  start = time()
  for i in xrange(1, n+1):
    if i == n: break
    num = i*i
    for j in xrange(i+1, n+1):
      num += j*j
      if num >= max_num: break 
      if is_pal(num):
        nums.add(num)
  print sum(nums)
  print time()-start

#returns the max n such that n^2+(n-1)^2 = x
def max_n(x):
  return int(.5*(1+(2*x-1)**.5))

#def is_pal(n): return str(n) == str(n)[::-1]

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
