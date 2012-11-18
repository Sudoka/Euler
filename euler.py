#!/usr/bin/python -tt
import re
import sys
import time

class euler:

  def add(self, x, y):
    return x+y

  #takes parameter n, and finds primes up to and including n
  def primes(self, n):
    mults = set()
    primes = []

    for i in xrange(2, n+1):
        if i not in mults:
            primes.append(i)
            mults.update(xrange(i*i, n+1, i))
    return primes
  


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
