# https://www.youtube.com/watch?v=lOzyQgv71_4


from bs4 import BeautifulSoup
import re

with open("beautiful-soup/index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")


# change the attribute value
tag = doc.find("option")
tag['value'] = 'new value'
# tag['selected'] = 'false'
# tag['color']='blue'
# print(tag.attrs)  # give all the attri
# print(tag)

# search multiple tag name
# tagname = doc.find_all(["p", "div", "li"])
# print(tagname)

tagtext = doc.find_all(['option'], text="Postgraduate")
# print(tagtext)

tagtext = doc.find_all(['option'], value="postgraduate")
# print(tagtext)

# find class name
tagclass = doc.find_all(class_="btn-item")
# print(tagclass)

# use regular expression - impor re
tagregex = doc.find_all(text=re.compile("\$.*"))
print(tagregex)
for reg in tagregex:
    print(reg.strip())  # remove all the white space

print("===========")
# limit the number, show only one
taglimit = doc.find_all(text=re.compile("\$.*"), limit=1)
for limit in taglimit:
    print(limit.strip())  # remove all the white space

# save the update
tags = doc.find_all("input", type="text")
for tag in tags:
    tag['placeholder'] = "I changed you!"

with open("beautiful-soup/changed.html", "w") as file:
    file.write(str(doc))
