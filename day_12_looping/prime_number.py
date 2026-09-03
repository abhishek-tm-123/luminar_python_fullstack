"""
read num
set is_prime to True
repeat for i from 2 to num-1
    if num%i==0 then
        update is_prime to False

print is_prime 
"""
num = int(input("Enter a number: "))
is_prime = True
for i in range(2,num):
    if num%i==0:
        is_prime = False
        break

print(is_prime)