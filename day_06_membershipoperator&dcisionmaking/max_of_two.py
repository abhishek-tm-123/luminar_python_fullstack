"""
read two numbers display largest number

read number1
read number2
chk if number1 > number2 then
        display number1 is largest
    else 
        display number2 is largest 

"""

num1 = int(input("enter number1"))#10

num2 = int(input("enter number2"))#20

if num1 > num2:# 10>20 => F

    print("number1 is largest")

else:

    print("num2 is largest")