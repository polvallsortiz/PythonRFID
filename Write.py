#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
        codi_barres = raw_input('Codi barres: ')
        id_unic = raw_input('ID Unic: ')
        preu = raw_input('Preu: ')
        print("Now place your tag to write")
        reader.write(codi_barres + "\t" + id_unic + "\t" + preu)
        print(codi_barres + "\t" + id_unic + "\t" + preu)
        print("Written")
finally:
        GPIO.cleanup()
