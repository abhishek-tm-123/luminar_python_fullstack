"""
    *
   **
  ***
 ****
*****

"""

for row in range(5,0,-1):
    for space in range(row-1):
        print(" ",end=" ")
    for col in range((5-row)+1):
        print("*",end=" ")
    print()