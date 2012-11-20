#!/usr/bin/python -tt
import re
import sys
import time

#takes parameter n, and finds primes up to and including n
def primes(n):
  mults = set()
  primes = []
  for i in xrange(2, n+1):
    if i not in mults:
      primes.append(i)
      mults.update(xrange(i*i, n+1, i))
  return primes
#returns the nth fibonacci number
def nth_fib(self, n):
  return int(round((1.6180339**n - (-0.6180339)**n)/2.236067))

#checks if a number is a palindrome
def is_pal(n): return str(n) == str(n)[::-1]

#returns the greatest common denominator (euclid's algorithm)
def gcd(a,b):
  if b > a:
    (a, b) = (b, a)
  while b != 0:
    (a, b) = (b, a%b)
  return a
