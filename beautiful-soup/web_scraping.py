# https://www.youtube.com/watch?v=gRLHr664tXA



from bs4 import BeautifulSoup
import requests

with open('beautiful-soup/index.html', 'r') as f:
    doc = BeautifulSoup(f, "html.parser")

# print(doc.prettify())

# find tag
tag = doc.title
# print(tag)
# print(tag.string)

# print("======")

tag.string = 'hello'
# print(tag)
# print(doc)

# print("======")

# find all the p tag
tags = doc.find_all("p")
# tags = doc.find_all("p")[0] #find first p tag
# print(tags)

tag1 = doc.find_all("p")[0]
# print(tag1.find_all('b'))

# pip install request - to access the website
# HTML From Website
url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"
result = requests.get(url)
# print(result.text)

# to get the html doc for that website by using beautiful soup
doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())

# to find the price of that item in that website
prices = doc.find_all(text='$')
parent = prices[0].parent
strong = parent.find("strong")
# print(strong.string)
