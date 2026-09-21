"""
Two pair sum - Two pointer


arr=[1,2,3,4,5,6]

target = 7

set left as 0

set right as len(arr)-1

repeat while left<right:
    set curr_sum as arr[left] +arr[right]

    case1: check target == curr_sum then display arr[left] ad arr[right] as pair and exit
    case2: check curr_sum>target then update right as right -1
    case3: check curr_sum<target then update left as left-1
"""


arr=[1,4,2,3,5,6,8,7]

target=11
arr.sort()

left = 0

right=len(arr)-1

while(left<right):
    curr_sum = arr[left] +arr[right]

    if curr_sum == target :
        print(arr[left],arr[right],"pair")
        break
    elif curr_sum>target :
        right-=1
    elif curr_sum<target:
        left+=1
