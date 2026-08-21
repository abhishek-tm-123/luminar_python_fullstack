"""
Circle: Multiply pi (π) by the radius squared (A = π r²).


set pi as 3.14

read radius

set area as pi*(radius**2)

display area
"""


pi = 3.14

radius = int(input("enter radius "))

area = pi * (radius**2)

print("area of circle is",area)