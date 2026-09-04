for row in range(1,5):
    for col in range(1,6):
        if col%2==0:
            print("E",end=" ")
        else:
            print("O",end=" ")
    print()