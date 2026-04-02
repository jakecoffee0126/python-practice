
# with close()
'''
file = open("python-functions/test.txt", "w")
file.write("Hello, World!")
file.close()
'''

# without close() instead of 'with'
with open("python-functions/newfile.txt", "w") as file:
    file.write("Hello, this is a new file!")


with open("python-functions/newfile.txt", "r") as file:
    text = file.read()
    print(text)
