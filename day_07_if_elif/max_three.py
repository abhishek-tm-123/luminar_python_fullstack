"""
read three numbers num1,num2,num3 
display largest amoung three numbers

read num1
read num2
read num3

chk if num1>num2 and num1>num3 then display num1 is largest

chk elif num2>num1 and num2>num3 then display num2 is largest

chk elif num3>num1 and num3>num2 then display num3 is largest

"""


num1 = int(input("enter number1"))

num2 = int(input("enter number2"))

num3 = int(input("enter numbe3"))

if num1 > num2 and num1>num3: 
    print("num1 is largest")

elif num2>num1 and num2>num3:

    print("num2 is largest")

elif num3>num1 and num3>num2:

    print("num3 is largest")


