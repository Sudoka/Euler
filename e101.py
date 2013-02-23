#!/usr/bin/python -tt
import re
import sys
import numpy as np

def main():
  P = [[0 for i in xrange(11)] for j in xrange(11)]
  for i in xrange(10):
    for j in xrange(10):
      P[i][j] = i**j
  vals = get_vals(np.poly1d([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]))
  #vals = get_vals(np.poly1d([1, 0, 0, 0]))
  K = 10
  BOP = 0
  for k in xrange(1, K+1):
    p = get_poly(P, vals[:k], k)
    _k = k
    num = p(_k+1)
    while num == vals[_k]:
      _k += 1
      num = p(_k+1)
    print k, int(num)
    BOP += num
  print int(BOP)

def get_vals(p, numvals=20):
  return [p(i) for i in xrange(1, numvals)]

#given n and k
def get_poly(P, vals, k):
  M = []
  while len(M) < k:
    for i in xrange(1, k+1):
      row = []
      for j in xrange(k, 0, -1):
        row.append(P[i][j-1])
      M.append(row)
  b = np.array(vals)
  a = np.array(M)
  return np.poly1d(np.linalg.solve(a, b))



# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
