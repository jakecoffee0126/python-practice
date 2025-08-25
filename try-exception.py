# https://youtu.be/rfscVS0vtbw?t=11057

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
