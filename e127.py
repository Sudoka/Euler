#!/usr/bin/python -tt
import re
import sys
from euler import *
from scipy import special as sp
def main():
  primes = [3] + e.primes(10000)[3:]

  print sum_scores(5, 10000, primes)

def sum_scores(start, stop, primes):
  score = 0
  for i in xrange(start, stop+1):
    k = get_k(i)
    # k / gcd(i, k) reduces k, and then we see if that is a term fraction
    if is_term(k/gcd(i,k), primes):
      score -= i
    else:
      score += i
  return score
  
def gcd(a,b):
  if b > a:
    (a, b) = (b, a)
  while b != 0:
    (a, b) = (b, a%b)
  return a

def is_term(n, primes):
  for prime in primes:
    if prime > n:
      return True
    if n%prime == 0:
      return False
  return True
    

# maximum of (n/k)**k occurs when k = n/e
# this ia because max critical point happens at d/dx (n/k)**k = 0
# which evals to (n/k)**k * (log(n/k)-1) = 0
# which evals to ln(n/k) = 1
# solving for k we get k = n/e
def get_k(n):
  return int( round(n / 2.71828182845904523536) )

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
