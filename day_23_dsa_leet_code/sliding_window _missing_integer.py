"""
arr = [1,3,2,5,4,7]

sort arr

arr = [1,2,3,4,5,7]
       l r

l=0
r=l+1
find diff between arr[l] and arr[r] is not 1 if true
    element is missing missing element is arr[l]+1
if false
    l=l+1
"""


"""arr = [1,3,2,5,4,7]

arr.sort()

l=0

while (l<len(arr)-1):

    r=l+1

    difference = arr[r] - arr[l]

    if difference!=1:
        print("missing number ",arr[l]+1)
        break
    else:
        l+=1"""


arr = [1,2,3,4,6]

arr.sort()

l=0

while l<len(arr)-1:
    r=l+1

    diff = arr[r] - arr[l]

    if diff != 1 :
        print("missing element :", arr[l]+1 )
        break
    else:
        l+=1