
# You can choose to import only parts from a module, by using the from keyword.
# Import only the person1 dictionary from the module:
# When importing using the from keyword,
# do not use the module name when referring to elements in the module.
# Example: person1["age"], not mymodule.person1["age"]

from modules import person1

print(person1["age"])
