# Convert from JSON to Python
# json.loads()

# Convert from Python to JSON
# json.dumps()


import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)
print(y["age"])


# a Python object (dict)
x2 = {
    "name": "John",
    "age": 42,
    "city": "Kansas"
}

# convert into JSON
y2 = json.dumps(x2)

# the result is a JSON string
print(y2)


print(json.dumps({"name": "Jake", "age": 42}))
print(json.dumps(["apple", "bananas", "kiwi"]))
print(json.dumps(("this", "is", "tuple")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


x3 = {
    "name": "Josh",
    "age": 42,
    "married": True,
    "divorced": False,
    "children": ("Allen", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x3))
print("============")
# You can also define the separators, default value is (", ", ": "),
# which means using a comma and a space to separate each object,
# and a colon and a space to separate keys from values:
print(json.dumps(x3, indent=4, separators=(". ", "= "), sort_keys=True))
