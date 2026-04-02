
# without using list function
names = ["Alice", "Bob", "Charlie", "David"]
ages = [30, 25, 35, 20]

# print(min(len(names), len(ages)))

# without zip function
# 'min', if there is extra name or age in the liSt, it will be ignore
for idx in range(min(len(names), len(ages))):
    name = names[idx]
    age = ages[idx]

    print(f"{name} is {age} years old")

print("===============")

# with zip function
names2 = ["Alice", "Bob", "Charlie", "David", "Jake"]
ages2 = [30, 25, 35, 20]
gender = ["F", "M", "F"]
combined = list(zip(names, ages, gender))
# only print out 3, because gender only has three list items
print(f"combined: {combined}")

combined = list(zip(names2, ages2))
for names2, ages2 in combined:
    print(f"{names2} is {ages2} years old")
