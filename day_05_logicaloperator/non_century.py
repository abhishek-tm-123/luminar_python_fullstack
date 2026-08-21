"""
q2)read a year and chk year not divisible by 100 and divisible by 4


read year

set is_leap_year as year%100 != 0 and year%4==0

display is_leap_year
"""

year = int(input("enter year...."))

is_leap_year = year%100!=0 and year%4==0

print(is_leap_year)

"""
membership operator, identity operator

"""

