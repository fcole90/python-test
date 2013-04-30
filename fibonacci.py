#! /usr/bin/env python

n = int(raw_input('Fibonacci:'))
print "Elaborazione di Fib(" + str(n) + ") in corso..."

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
print str(fibonacci(n))
