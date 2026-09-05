"""
gcd of two numbers

read num1, num2
set small_num to the minimum of num1 and num2
set gcd to 1
repeat for i from 2 to small_num
    if num1%i==0 and num2%i==0 then
        update gcd to i

print gcd
"""

num1=int(input("Enter a number: "))
num2=int(input("enter second number: "))
small_num=min(num1,num2)
gcd=1

for i in range(2,small_num+1):
    if num1%i==0 and num2%i==0:
        gcd=i

print(gcd)





num1=int(input("enter n1:"))
num2=int(input("enter n2:"))
min_num = min(num1,num2)
gcd = 1
for i in range(1,min_num+1):
    if num1%i==0 and num2%i==0:
        gcd=i

print(gcd)