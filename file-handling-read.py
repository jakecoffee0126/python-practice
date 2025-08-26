# https://www.w3schools.com/python/python_file_open.asp

f = open('demo.txt')
# print(f.read())


print("======check if readable with 'r' mode======")

y = open('demo.txt', 'r')
print(y.readable())
y.close()

print("======check if readable with 'rw' mode======")
# y = open('demo.txt', 'w')  # this will clean the data
# print(y.readable())
# y.close()

print("======readline======")

# readline(), print our the first line of the file
print(f.readline())
# By calling readline() two times, you can read the two first lines:
print(f.readline())
f.close()

print("======readlines, read all the lines======")
# readlines() is to read all the copy in the file, and put it to the array
ff = open('demo.txt')
print(ff.readlines())
ff.close()

print("======readlines, read specific line======")
# readlines() is to read all the copy in the file, and put it to the array
fff = open('demo.txt')
print(fff.readlines()[2])
fff.close()

print("======print out all the lines with loop======")
loof = open('demo.txt', 'r')
for alllines in loof.readlines():
    print(alllines)
loof.close()

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
