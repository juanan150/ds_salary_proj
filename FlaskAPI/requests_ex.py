# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 20:49:58 2021

@author: JUAN.QUIROZ
"""

import requests
from data_input import data_in

URL = 'http://127.0.0.1:5000/predict'
headers = {'Conten-Type': 'application/json'}
data = {'input': data_in}

r = requests.get(URL, headers = headers, json = data)

r.json()
