# https://github.com/techwithtim/Beautiful-Soup-Tutorial
# https://youtu.be/lC6mucyD17k?t=57


from bs4 import BeautifulSoup
import requests

url = 'https://coinmarketcap.com/'
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
print(tbody)
