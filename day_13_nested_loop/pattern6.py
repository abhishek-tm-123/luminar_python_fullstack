for row in range(1,4):
    for col in range(1,7):
        if col%2!=0:
            print(row,end="  ")
        else:
            print("E",end="  ")
    print()