n = int(input())
m = int(input())

# Initialize the sign as a list of empty strings
sign = [""] * n

# Loop through each row of the sign
for i in range(n):
    # Calculate the number of asterisks needed for the left side of the sign
    left_asterisks = abs(m - i)

    # Calculate the number of spaces needed for the middle of the sign
    middle_spaces = 2 * (n - i - 1) - 1

    # Calculate the number of asterisks needed for the right side of the sign
    right_asterisks = abs(m - i)

    # Add the left asterisks, middle spaces, and right asterisks to the current row of the sign
    row = "*" * left_asterisks + " " * middle_spaces + "*" * right_asterisks

    # Add the row to the sign
    sign[i] = row

# Print the sign
for row in sign:
    print(row)
