input_file = "input.txt"
output_file = "output.txt"

# Count total number of lines
with open(input_file, "r") as file:
    line_count = 0

    for line in file:
        line_count += 1

print("Total number of lines:", line_count)


# Read the first two lines
first_two_lines = []

with open(input_file, "r") as file:
    for i in range(2):
        line = file.readline()

        if line == "":
            break

        first_two_lines.append(line)


# Write the first two lines into a new file
with open(output_file, "w") as file:
    file.writelines(first_two_lines)

print("First two lines have been written to", output_file)