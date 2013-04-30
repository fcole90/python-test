#!/usr/bin/env python
# ---------Monty Hall Problem Solver--------
# Is the Monty Hall Problem solution correct?
from random import randint

print 'This is Monty Hall Problem Solver'
print 'Please, wait a moment while working...'

def noPresChoice(choice, presChoice):
  choice = choice 
  presChoice = presChoice 
  j=0 
  
  while (j==choice) or (j==presChoice):
    j = j + 1
  
  finalChoice = j
  return finalChoice
    
  

Awin=0
Bwin=0
Cwin=0

AchoicedFirst=0
BchoicedFirst=0
CchoicedFirst=0

changed=0
won=0

winWhenChanged=0
winWhenNotChanged=0

i=0 #Declared iterator and set to 0
while i<1:  #Start the cicle
  
  door = randint(0,2) #This is a random number from 0 to 2 (3 scenarios)
  #Conditions based on the three scenarios
  if door == 0:
    A=1
    B=0
    C=0
  elif door == 1:
    A=0
    B=1
    C=0
  else:
    A=0
    B=0
    C=1
           
  i = i + 1     #Iterator        
  print "---------------------------------------------------------"
  print str(A) + " " + str(B) + " " + str(C) + " This is the solution #" + str(i) + ", now the player is asked to choice a door... "
  
  #First choice
  choice = randint(0,2)
  print "The player choose the door #" + str(choice+1)
  if choice == door:
    print "Wow, the player is winning!"
    W1=1
  else:
    print "The player is loosing, but.. Who knows!"
    W1=0
    
  #Presenter choice
  print "Now the presenter will open a wrong door..."
  if choice == 0:
    presChoice = randint(1,2)
  elif choice == 2:
    presChoice = randint(0,1)
  else:
    tempChoice = randint(0,1) #random temporaneo per impostare 0 o 2
    if tempChoice == 0:
      presChoice = 0
    else:
      presChoice = 2
  print "The presenter choices to open the door #" + str(presChoice+1)
  
  
  #Second choice
  print "Now the player is asked to change or mantain his choice."
  change = randint(0,1)
  if change == 0:
    print "The player choices to mantain his choice."
    finalChoice = choice
  else:
    print "The player choices to change his choice."
    finalChoice = noPresChoice(choice, presChoice)
    print "The player selects now the door #" + str(finalChoice+1)
    
  if finalChoice == door:
    print "The player won the prize of the Monty Hall Show."
  else:
    print "The player has lost!"
    
  print "---------------------------------------------------------"
  
  
  
  #Ends the cycle
  
print 'Completed!'

