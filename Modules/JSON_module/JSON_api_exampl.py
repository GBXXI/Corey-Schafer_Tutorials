
import json
from urllib.request import urlopen

with urlopen('https://finance.yahoo.com/webservice/v1/sumbols/allcurrencies/quote?format=json') as response:
    source = response.read()

data = json.loads(source)

print(json.dumps(data, indent=2))
