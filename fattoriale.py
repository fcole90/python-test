#! /usr/bin/env python

n = int(raw_input('Fattoriale:'))
print "Elaborazione di " + str(n) + "! in corso..."

def fattoriale(n):
    if n==0:
        return 1
    else:
        fattorialeNMenoUno = fattoriale(n-1)
        result = n * fattorialeNMenoUno
        return result
        
print str(fattoriale(n))
