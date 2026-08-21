"""
Trapezium: Add parallel sides (a + b), multiply by height (h), and divide by two (\(A = \frac{1}{2}(a + b)h\)).


read a

read b

read h

set area as 0.5(a+b)*h
"""

a =  int( input("enter side1 "))
b =  int( input("enter side2 "))
height =  int( input("enter height "))

area = 0.5 * (a+b)*height

print("area of trazpezium is",area)
