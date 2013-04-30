#!/usr/bin/env python
#mhpss for mhps
from random import randint

diff = randint(0,2)
if diff == 0:
  A=1
  B=0
  C=0
elif diff == 1:
  A=0
  B=1
  C=0
else:
  A=0
  B=0
  C=1
  
print str(A) + " " + str(B) + " " + str(C) + " This is the solution, now the player goes..."
