#!/usr/bin/python

from sense_hat import SenseHat
import time

sense = SenseHat()

red = (255, 0, 0)
pink = (255, 102, 178)
green = (0, 255, 0)
blue = (0, 0, 255)
seila = (0, 255, 255)

nome = (list("LAURA"))

X = [255, 0, 0]  # Red
O = [0, 0, 0]  # None

warn2 = [
O, O, X, X, X, X, O, O,
O, X, O, O, O, O, X, O,
X, O, X, O, O, X, O, X,
X, O, O, O, O, O, O, X,
X, O, X, O, O, X, O, X,
X, O, O, X, X, O, O, X,
O, X, O, O, O, O, X, O,
O, O, X, X, X, X, O, O
]

warn = [
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X
]

heart = [
O, O, O, O, O, O, O, O,
O, X, X, O, O, X, X, O,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
O, X, X, X, X, X, X, O,
O, O, X, X, X, X, O, O,
O, O, O, X, X, O, O, O,
O, O, O, O, O, O, O, O
]

def warning():
	print("Warning")
        for a in range(0, 5):
                sense.set_pixels(warn)
                time.sleep(0.2)
                sense.clear()
                time.sleep(0.2)
        time.sleep(1)

def contagem():
	c = 5
	while(c > 0):
		sense.show_letter(str(c), text_colour=green)
		print(str(c))
		c = c - 1
		time.sleep(1)

def perguntanome():
	print("CLARA OU LAURA") 
	sense.show_message("CLARA OU LAURA", text_colour=blue, scroll_speed=0.05)

def interrogacao():
	for i in range(5):
		sense.show_letter("?", text_colour=seila)
		print("?")
		time.sleep(0.5)
		sense.clear()
		time.sleep(0.5)
	time.sleep(1)
		
def suspense():
	print("E O NOME ESCOLHIDO FOI.....")
	sense.show_message("E O NOME ESCOLHIDO FOI.....", text_colour=blue, scroll_speed=0.05)
	time.sleep(1)

def spell():
	for n in (nome):
		sense.show_letter(n, text_colour=pink)
		print(n)
		time.sleep(0.5)
	time.sleep(1)
	sense.clear()

def finaliza():
	for x in range(0, 5):
		sense.set_pixels(heart)
		print("Coracao")
		time.sleep(0.5)
		sense.clear()
		time.sleep(0.5)
#	time.sleep(1)

def rindo():
	sense.set_pixels(warn2)
	print("Smile")
	time.sleep(5)

def limpa():
	sense.clear()
	print("Limpando tudo")

limpa()
warning()
contagem()
perguntanome()
interrogacao()
suspense()
spell()
finaliza()
rindo()
limpa()


#except KeyboardInterrupt:
#	sense.clear()
