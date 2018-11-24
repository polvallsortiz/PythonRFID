
#!/usr/bin/env python
import RPi.GPIO as GPIO
import SimpleMFRC522
import time
import requests

reader = SimpleMFRC522.SimpleMFRC522()

while True:
        print("While")
        id, text = reader.read()
        if text:
                text = text.strip().split("\t")
                print(text)
                time.sleep(1)
                if len(text) != 3:
                        print("SCAN AGAIN THE PRODUCT")
                else:
                        r = requests.post("http://ordinadorcasa.no-ip.org:4105/checkout/item",data={'name': text[0], 'uid': text[1], 'price': float(text[2])})
                        print(r.status_code, r.reason)
        time.sleep(0.5)
        
