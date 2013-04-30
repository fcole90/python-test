#!/usr/bin/python -O
from Tkinter import *

class Finestra(Tk):

	def __init__(self):
		"""Costruttore della classe Finestra
		"""
		Tk.__init__(self)
		self.title('Ciao da TkInter')
		self.geometry("%dx%d" % (220, 150))

		# creo il bottone
		b = Button(self, text='Ciao mondo !', command=self.helloWorld)
		b.place(x=15, y=15)
		
		# registro l'evento di chiusura della finestra		
		self.protocol('WM_DELETE_WINDOW', self.__chiudi)
		
	def mostra(self):
		"""Visualizza la finestra
		"""
		# mando in loop l'applicazione
		self.mainloop()
 
	def helloWorld(self):
		"""Stampa sullo standard output la stringa 'Hello world !'
		"""
		print 'Ciao mondo !'

	def __chiudi(self):
		"""Chiude l'applicazione alla chiusura della finestra
		"""
		self.destroy()
		
		
if __name__ == '__main__':
	f = Finestra()
	f.mostra()
