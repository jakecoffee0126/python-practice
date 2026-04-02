
tasks = ["Write report", "Attend meeting", "Review code", "Submit timesheet"]

# without using enumerate
for index in range(len(tasks)):
    task = tasks[index]
    print(f"{index + 1}.{task}")

print("=============")
# with enumerate
for index, task in enumerate(tasks):
    print(f"{index + 1}.{task}")


print(list(enumerate(tasks)))
