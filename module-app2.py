
import modules as mo
import platform  # bult in moduels

mo.greeting("Zoe")

x = platform.system()
print(x)

# There is a built-in function to list
# all the function names (or variable names) in a module. The dir() function:
x = dir(platform)
print(x)
