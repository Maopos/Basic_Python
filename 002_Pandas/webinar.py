import pandas as pd
import requests
import statistics


r = requests.get("https://api.recursospython.com/dollar")

datos = pd.DataFrame([100, 200, 300, 400, 500], index = ['Cafe', 'Oro', 'Petroleo', 'Platino'])

print(datos)

