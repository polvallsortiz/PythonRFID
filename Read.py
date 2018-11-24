#!/usr/bin/env python

from Tkinter import *
import tkFont
import RPi.GPIO as GPIO
import SimpleMFRC522
import time
import json

reader = SimpleMFRC522.SimpleMFRC522()

win = Tk()

win.title("First GUI")
win.geometry('800x480')

myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')

products = {}

f = Frame(win)
f.pack()


def my_mainloop():
        print("MAIN")
        id, text = reader.read_no_block()
        if text:
                text = text.strip().split("\t")
                print(text)
                time.sleep(1)
                if len(text) != 3:
                        print("SCAN AGAIN THE PRODUCT")
                else:
                        if text[0] not in products:
                                products[text[0]] = set()
                                products[text[0]].add(text[1])
                        else:
                                if text[1] not in products[text[0]]:
                                        products[text[0]].add(text[1])
                                else:
                                        products[text[0]].remove(text[1])
                                        if len(products[text[0]]) == 0:
                                                products.pop(text[0],None)
                        recalculate()                          
                                
        print(products)
        win.after(1000, my_mainloop)



def recalculate():
        text = ""
        f = Frame(win)
        f.destroy()
        f = Frame(win)
        f.pack()
        for values in products:
                codi = str(values)
                quantitat = str(len(products[values]))
                fila = codi + " " + quantitat + "\n"
                text += fila
                w = Label(f, text = text)
                w.pack()
                
                


def exitProgram():
	print("Exit Button pressed")
        GPIO.cleanup()
	win.quit()

exitButton  = Button(win, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 6) 
exitButton.pack(side = BOTTOM)

my_mainloop()

win.mainloop()



