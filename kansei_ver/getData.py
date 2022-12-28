# -*- coding: utf-8 -*-
import requests
import json

def getData():
    #url = "https://script.google.com/macros/s/AKfycbwlwCtvzQuE8Et2__ZiXw2GOwzCDs3fvjSw312q-AT5Mt5x3BU/exec"
    url = "https://script.google.com/macros/s/AKfycbwlwCtvzQuE8Et2__ZiXw2GOwzCDs3fvjSw312q-AT5Mt5x3BU/exec"
    response = requests.get(url)
    return json.loads(response.text)

DB = getData()
#for db in DB:
 #   if db["pass2"] != "":
  #      print(db)