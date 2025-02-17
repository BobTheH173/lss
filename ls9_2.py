import requests

response = requests.get('https://coinmarketcap.com')
print(response.content)
print(f"Data type - {type(response.content)}")
