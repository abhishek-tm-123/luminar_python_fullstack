"""arr = [2,3,4,5,6]

target = 9

for num in arr:

    difference = target - num

    if difference in arr:

        print(difference,num,"are the pair")
        break

else:

    print("no pair")"""


arr = [1,2,3,4,5,6]
trgt = 5
for num in arr:

    diff = trgt-num

    if diff in arr:
        print(diff,num)
        break
else:
    print("no pair")