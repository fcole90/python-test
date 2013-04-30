#!/usr/bin/env python3
#author Fabio Colella fcole90@gmail.com
#version 1.4.0 it


#creo la classe
class name:

    
    
    #definizione del metodo say()
    def say(self):
        print('\n')
        print('Grazie, continuiamo...\n')
        name = input('Come ti chiami?\n')
        name = name[0].upper() + name[1:]
        greet = '''\nCi vedremo presto, ''' + name + '!'
        message = '''
           ______
          |======|
         |========|  	 _____________
         ////\\\\\\\\\\\\    /               \\
         |/o\\ /o\\ |   | MUAHAHAAHAHAHA! |
         /  /oo\\   \\   \\ ______________/
        |   _____   |  |/
      ___\\  \\___/  /___
  ___/    \\_______/      \\___'''
        version = 'test.py by fcole90 version 1.4.0 it'
        print(message + greet)

#fine della classe

#parte procedurale
line = str(input('Sei sicuro di voler continuare?\n'))
lowline = line.lower()

if lowline in ('si' , 's' , 'y' , 'yes' , 'ok'):
    name = name() #istanzio la classe, le parentesi sono obbligatorie
    name.say()
else:
    print('KABOOOOOOOOOOOOOOOOOM!\n')
    exit()
    
