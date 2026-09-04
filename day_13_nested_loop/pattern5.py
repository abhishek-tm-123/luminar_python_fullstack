for row in range(1,5):
    for col in range(1,5):
        if col%2==0:
            print(col,end="  ")
        else:
            print("*",end="  ")
    print()