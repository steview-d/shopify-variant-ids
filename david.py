# Deadly Accurate Variant Id Detector

import json, re, requests
from bs4 import BeautifulSoup

# temp vars
url = 'https://e-liquids.com/collections/50-50-vape-juices/products/six-licks-50-50-melon-on-my-mind-10ml'

# var meta = {"product":

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
result = str(soup.find('script', text=re.compile('var meta = {"product":')))
foo = result.split('var meta = ')[1].split('for (var attr in')[0]
json_data = json.loads(foo[:-2])
print(type(json_data))
print(json_data)