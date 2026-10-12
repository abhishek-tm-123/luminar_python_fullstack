
def moveZeroes( nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    index=0
    for _ in range(len(nums)):
        if nums[index] == 0:
            num = nums.pop(index)
            nums.append(num)
        else:
            index+=1

def moveZeros1(nums:list[int])->None:
    l=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[l],nums[i]=nums[i],nums[l]
            l+=1
    print(nums)

moveZeros1([2,0,3,0,1])