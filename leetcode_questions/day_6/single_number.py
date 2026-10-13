def single_number(nums:list[int])->int:
    res = 0
    for num in nums:
        res = res ^ num
    return res

print(single_number([2,4,2,1,3,3,1]))