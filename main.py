# Problem: Compute an estimate of total monthly production for competitor
# Input: serial numbers for month, a list of integers
serial_number_one = input("What is the first serial number?")
serial_number_one = int(serial_number_one)  # converts String input to integer
serial_number_two = input("What is the second serial number?")
serial_number_two = int(serial_number_two)  # converts String input to integer
serial_number_three = input("What is the third serial number?")
serial_number_three = int(serial_number_three)  # converts String input to integer
# assigns input serial numbers to a list
serial_numbers = [serial_number_one, serial_number_two, serial_number_three]

# set largest_serial to non-empty list
largest_serial = 1

# Sub-problem: find the highest serial number
for position in serial_numbers:
    if position > largest_serial:
        largest_serial = position

# Sub-problem: Count the number of bears collected for the month
# number_bears = 5
number_bears = input("How many bears were collected this month?")
number_bears = int(number_bears)
for item in serial_numbers:
    number_bears = number_bears + 1

# Sub-problem: Compute the estimate using a pre-defined formula
result_one = largest_serial - number_bears
result_two = result_one // number_bears
estimate_total = result_two + largest_serial

# print total monthly production estimate
print('The monthly production estimate is', estimate_total)