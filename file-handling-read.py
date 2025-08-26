# https://www.w3schools.com/python/python_file_open.asp

f = open('demo.txt')
# print(f.read())

print("======readline======")

# Then you do not have to worry about closing your files,
# the with statement takes care of that.
print(f.readline())
# By calling readline() two times, you can read the two first lines:
print(f.readline())
f.close()

print("======with statement======")
# Use 'with' statement, then you do not have to worry about closing your files,
# the with statement takes care of that.
with open('demo.txt') as f:
    print(f.read())

print("======looping======")

# By looping through the lines of the file,
# you can read the whole file, line by line:
with open('demo.txt') as f:
    for x in f:
        print(x)


print("======10 first characters======")
# Return the 5 first characters of the file:
with open("demo.txt") as f:
    print(f.read(10))
