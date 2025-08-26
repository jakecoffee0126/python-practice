# https://youtu.be/rfscVS0vtbw?t=11057
# https://www.w3schools.com/python/python_try_except.asp


# it will throw out an error when you are not entering the int
# number = int(input("Enter a number: "))
# print(number)


try:
    number = int(input("Enter a number: "))
    print(number)

except ZeroDivisionError as err:  # 10/0
    print("Divided by zero")
    print(err)
except ValueError:
    print("Invalid Input")


# You can use the else keyword to define a block
# of code to be executed if no errors were raised:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")


# The finally block, if specified, will be executed regardless
#  if the try block raises an error or not.
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")


try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
