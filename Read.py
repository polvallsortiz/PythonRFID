#!/usr/bin/env python

from Tkinter import *
import ttk
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
myFont2 = tkFont.Font(family = 'Helvetica', size = 20, weight = 'normal')

products = {}

products_price = {}

x = Frame(win)
x.pack()

f = Frame(win)
f.pack()




def my_mainloop():
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
                                products_price[text[0]] = float(text[2])
                                products[text[0]].add(text[1])
                                win.configure(background='green')
                        else:
                                if text[1] not in products[text[0]]:
                                        products[text[0]].add(text[1])
                                        price = products_price[text[0]]
                                        price = price + float(text[2])
                                        products_price[text[0]] = price
                                        win.configure(background='green')
                                else:
                                        products[text[0]].remove(text[1])
                                        price = products_price[text[0]]
                                        price = price - float(text[2])
                                        products_price[text[0]] = price
                                        if len(products[text[0]]) == 0:
                                                products.pop(text[0],None)
                                        win.configure(background='red')                                        
                        recalculate()                          
                                
        win.after(1000, my_mainloop)



def recalculate():
        text = ""
        for widget in f.winfo_children():
                widget.destroy()
        for values in products:
                print(values)
                codi = str(values)
                quantitat = str(len(products[values]))
                price = str(products_price[values])
                fila = codi + " " + quantitat + " " + price + "\n"
                text += fila
        w = Label(f, text = text, font = myFont)
        w.pack()
                
                
def finalizeShop():
        print("Finalize cart")
        for widget in f.winfo_children():
                widget.destroy()
        products.destroy()
        products = {}
        print(products)
        products_price = {}
        print(products_price)
        for widget in f.winfo_children():
                widget.destroy()
        


def exitProgram():
	print("Exit Button pressed")
        GPIO.cleanup()
	win.quit()

finalizeButton  = Button(win, text = "Finalize my shop", font = myFont2, command = finalizeShop, height =2 , width = 6) 
finalizeButton.pack(side = BOTTOM)

exitButton  = Button(win, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 6) 
exitButton.pack(side = BOTTOM)

my_mainloop()

win.mainloop()



