"""
read a number and evaluate last_digit in range of 3 to 7

read number

set last_digit as number % 10

set is_in_range as last_digit > 3 and last_digit < 7

display is_in_range

"""

number = int(input ("enter number.... "))

last_digit = number % 10

is_in_range = last_digit > 3 and last_digit < 7

print(is_in_range)

