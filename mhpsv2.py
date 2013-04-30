#!/usr/bin/env python
# ---------Monty Hall Problem Solver--------
# Is the Monty Hall Problem solution correct?
# author: Fabio Colella <fcole90@gmail.com>
# version: 1.1.0
###############CHANGELOG#####################
# |19-04-2013 14:38| added input to choice a number of loops 1.0.1
# |19-04-2013 15:02| added info on Monty Hall problem and statistics 1.0.2
# |19-04-2013 16:02| bugfix to prevent runtime error n/0 at line 138 (or below) 1.1.0
#############################################
# Licensed under LGPL


from random import randint


print 'This is Monty Hall Problem Solver'
print 'Please, wait a moment while working...'
print 'How many games do you want to play?'
k=0
while True:
  if k >= 5:
     print 'Ok, I understand that this may seem difficult..'
     print 'Only the following are legal!'
     print '1 2 3 4 5 6 7 8 9 0'
     print 'And any combination of them:'
     print 'Es: 10, 1000, 999, 31416'
     print 'And they need to be integer numbers..'
     print 'You cannot perform just a part of the loop!'
     print 'Now please...'
     k =0
  number = raw_input('Enter a number:')
  try:
      times = int(number)
  except ValueError:
      print "You didn't tape a number!"
      k += 1      
      continue
  break

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
while i<times:  #Start the cicle
  
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
  presChoice = noPresChoice(door, choice)
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
    winner = 1
  else:
    print "The player has lost!"
    winner = 0
    
  print "---------------------------------------------------------"
  
  if (change == 1) and (winner == 1):
   winWhenChanged += 1
  elif (change == 0) and (winner == 1):
   winWhenNotChanged += 1
   
  if change == 1:
   changed +=1
   
  if winner == 1:
    won += 1
  
  #Ends the loop

#Percentuals (edited to prevent runtime error n/0)
if won>0:
  percWWC = (100.0/won)*winWhenChanged
  percWWNC = (100.0/won)*winWhenNotChanged
else:
  percWWC = 0
  percWWNC = 0


  
print 'Completed after ' + str(times) + ' loops !'
print 'Results:'
print '--------------------------------------------'
print '|                  TOTAL                   |'
print '|------------------------------------------|'
print '| Win and Changed --------> (' + str(winWhenChanged) + ')'
print '| Win without changes-----> (' + str(winWhenNotChanged) + ')'
print '| Total Victories --------> (' + str(won) + ')'
print '--------------------------------------------'
print 'The Statistics say that changing the door'
print 'is more succesful than mantaining the same door.'
print 'Probabilities of victory are double when changing.'
print 'If you made a number of loops big enough you should'
print 'see that the statistics were correct'
print '--------------------------------------------'
print '|               PERCENTUALS                |'
print '|------------------------------------------|'
print '| Win and Changed ----------> (' + str(percWWC) + '%)'
print '| Win without changes-------> (' + str(percWWNC) + '%)'
print '--------------------------------------------'
print 'You can find more info about googling'
print 'Monty Hall problem'



