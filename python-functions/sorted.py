numbers = [4, 23, -5, 0, -33]
sorted_nums = sorted(numbers)
print(sorted_nums)

sorted_nums_reverse = sorted(numbers, reverse=True)
print(sorted_nums_reverse)


people = [
    {"name": "Alice", "age": 30},
    {"name": "Jake", "age": 22},
    {"name": "Zoe", "age": 3},
    {"name": "Yong", "age": 70},
]

sorted_people = sorted(people, key=lambda person: person["age"])
print(sorted_people)
