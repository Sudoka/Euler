#!/usr/bin/python -tt
import re
import sys
import euler as e
import matplotlib.pyplot as plt

def main():
  n = 100000
  squares = [i**2 for i in xrange(int(n**.5)+1)]
  score = 0
  nums = []
  for num in squares:
    tmp = is_prog(num)
    if tmp != None:
      score += num
  print score

def is_prog(n):
  for i in xrange(2, int(n**.5)+1):
    t = [n%i, n/i, i]
    if is_same_ratio(sorted(t)):
      #print n, ' ', t
      return t
  return None

def is_same_ratio((a, b, c)):
  x = e.gcd(a, b)
  y = e.gcd(b, c)
  return (b/x == c/y and a/x == b/y)


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
