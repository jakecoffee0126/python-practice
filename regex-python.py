# https://www.w3schools.com/python/python_regex.asp

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("Yes, there is a match!")
else:
    print("No match")
