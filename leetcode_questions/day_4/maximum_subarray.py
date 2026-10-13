#nums = [-2,1,-3,4,-1,2,1,-5,4]
nums=[5,4,-1,7,8]
#nums=[1]
def maxSubArray(nums:list[int])->int:

    max_sum =0
    for gap in range(1,len(nums)+1):
        j=0
        while j+gap<=len(nums):
            curr_sum = sum(nums[j:j+gap])
            
            if curr_sum>max_sum:
                max_sum=curr_sum
            j+=1
        gap+=1

    return max_sum

def maxSubArray2(nums:list[int])->int:
    
    max_sum = 0
    curr_sum=0
    for num in nums:
        curr_sum = num + curr_sum
        if num > curr_sum:
            curr_sum=num
        if curr_sum>max_sum:
            max_sum=curr_sum
    return max_sum


print(maxSubArray(nums))

print(maxSubArray2(nums))

