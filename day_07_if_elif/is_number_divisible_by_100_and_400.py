

"""
read year

chk if year%100==0 and year%400==0: then display century leapyear
"""

year = int(input("enter year"))

if year%100==0 and year%400==0:

    print("century leap year")