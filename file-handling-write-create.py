# https://www.w3schools.com/python/python_file_write.asp
# https://www.w3schools.com/python/python_file_remove.asp

import os
with open('demo.txt', 'a') as f:
    f.write('\n' + "this is append copy")

# open and read the file after the appending:
with open('demo.txt') as f:
    # print(f.read())
    pass


# Overwrite Existing Content
with open('demo2.txt', 'w') as f:
    f.write("WOOPS! I have deleted the content!")

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
