# https://www.w3schools.com/python/python_file_write.asp
# https://www.w3schools.com/python/python_file_remove.asp

import os
with open('demo.txt', 'a') as f:
    f.write("\nthis is append copy")  # make sure to use '\n'

# open and read the file after the appending:
with open('demo.txt') as f:
    # print(f.read())
    pass


# Overwrite Existing Content
with open('demo2.txt', 'w') as f:
    f.write("WOOPS! I have deleted the content!")

# write a html
with open('index.html', 'w') as ff:  # it will auto to create a file if its not there
    ff.write("<h1>This is Jake</h1>")


# open and read the file after the appending:
with open("demo2.txt") as f:
    print(f.read())


'''create a new file'''
f = open("create-file.txt", 'x')


'''To delete a file, you must import the OS module,
and run its os.remove() function:
'''
# os.remove('create-file.txt')


'''Check if File exist'''
if os.path.exists('create-file.txt'):
    os.remove('create-file.txt')
else:
    print('The file does not exist')

'''Remove the folder "myfolder":'''
os.rmdir("myfolder")
