
"""
q1)read a year and chk year is divisble by both 100 and 400


read year

set is_divisble as year % 100 ==0 and year%400==0

display is_divisble

"""


year = int(input("enter year... "))

is_divisible = year%100==0 and year%400==0


print(is_divisible)