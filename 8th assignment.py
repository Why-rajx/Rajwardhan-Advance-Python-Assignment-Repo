with open("input.txt", "r") as data:
    content = data.readlines()

total_lines = len(content)

print("Total number of lines:", total_lines)

first_lines = content[:2]

with open("output.txt", "w") as result:
    result.writelines(first_lines)

print("First two lines have been written to output.txt")