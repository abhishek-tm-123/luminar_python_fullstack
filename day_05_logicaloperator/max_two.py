

"""
read two number num1 , num2 and evaluate num1 is larger than num2 and num1 is even

read num1
read num2

set is_num1_even_big as  num1 > num2 and num1%2==0

display is_num1_even_big
"""


num1 = int(input("enter num1 "))#16
num2 = int(input("enter num2 "))#18

is_even_big = num1>num2 and num1%2==0 #  16 > 18 and 16%2==0 => F 

print(is_even_big)