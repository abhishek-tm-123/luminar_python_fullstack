"""
question1: 

            #
            #
            #
            #
#   #   #   #  

answer:

for row in range(1,6):
    for col in range(1,5):
        if row==5 or col==4:
            print("#",end="  ")
        else:
            print(" ",end="  ")
    print()
          



question2:

#   #   #   #
            #
            #
            #
            #

answer:


for row in range(1,6):
    for col in range(1,5):
        if row==1 or col==4:
            print("#",end="  ")
        else:
            print(" ",end="  ")
    print()


question3:

#
#
#
#
#   #   #   #

answer:

for row in range(1,6):
    for col in range(1,5):
        if row==5 or col==1:
            print("#",end="  ")
        else:
            print(" ",end="  ")
    print()



question4:

#   #   #   #   #
#               #
#               #
#               #
#   #   #   #   #

answer:

for row in range(1,6):
    for col in range(1,6):
        if row==1 or row==5 or col==1 or col==5:
            print("#",end="\t")
        else:
            print(" ",end="\t")
    print()


question5:

1   2   3   4   5
1   2   3   4   5
1   2   3   4   5
1   2   3   4   5

answer:

for row in range(1,5):
    for col in range(1,6):
        print(col,end="  ")
    print()


question6

1   1   1   1
2   2   2   2   
3   3   3   3   
4   4   4   4   

answer:

for row in range(1,5):
    for col in range(1,6):
        print(row,end="  ")
    print()

  
"""