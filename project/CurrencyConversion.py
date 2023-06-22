import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.freecurrencyapi.com/v1/latest?apikey=API-KEY"

resp = requests.get(url)

print(resp.status_code)

import freecurrencyapi
client = freecurrencyapi.Client('API-KEY')

print(client.status())

# result = client.currencies(currencies=['EUR', 'USD'])
# print(result)


result = client.latest(["USD"])["data"]["EUR"]
print(result)
