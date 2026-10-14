def majorityElement(nums: list[int]) -> int:
    hashmap={}
   
    for num in nums:
        if num not in hashmap:
            hashmap[num]=1
        else:
            hashmap[num] = hashmap[num]+1
        if hashmap[num] > len(nums)/2:
            majority=num 
    print(hashmap)
    
        
    return majority
#boyer - moore voting algorithm
def majorityElement1(nums:list[int])->int:
    majority = 0
    count = 0
    for num in nums:
        if count == 0 :
            majority=num
        if num == majority:
            count+=1
        else:
            count-=1
    return majority

print(majorityElement1([2, 2, 1, 1, 1,1,1, 2, 2]))

assert majorityElement1([2, 2, 1, 1, 1,1,1, 2, 2]) == 1