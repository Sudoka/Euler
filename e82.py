#!/usr/bin/python -tt
import re
import sys
from euler import *

def main():
  e = euler()
  M = [map(int, line[:-1].split(','))for line in open('matrix.txt', 'r')]
  S = [[0 for i in xrange(len(M[0]))] for j in xrange(len(M))]
  for i in xrange(len(M)):
    S[i][0] = M[i][0]
  S[-1][1] = S[-1][0]+M[-1][1]
  S[0][1] = S[0][0]+M[0][1] 

  for k in xrange(1):
    for i in xrange(len(M)):
      for j in xrange(1, len(M[0])):
        if i+1 == len(M):
          S[i][j] = M[i][j] + min(S[i-1][j], S[i][j-1])
        elif i-1 < 0:
          S[i][j] = M[i][j] + min(S[i+1][j], S[i][j-1])
        else:
          S[i][j] = M[i][j] + min(S[i-1][j], S[i+1][j], S[i][j-1])
  print min([row[-1] for row in S])


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
