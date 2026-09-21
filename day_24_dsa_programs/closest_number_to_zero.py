"""
arr = [-2,-1,1,3,4]

set closest value as arr[0]

repaet for ech num in arr :
    check if abs(num)<abs(closest):
        update closest to num

        
if closest < 0 and abs(closest) in nums:    
    print(abs(closest))
else:
    print(closest)



"""

nums=[-2,-1,1,2]

closest = nums[0]

for num in nums:
    if abs(num) < abs(closest):
        closest = num

if closest < 0 and abs(closest) in nums:
    print(abs(closest))
else:
    print(closest)


nums = [-2,1,-1,4,2]
closest = nums[0]
for num in nums:
    if abs(num) < abs(closest):
        closest = num

if closest<0 and abs(closest) in nums:
    print(abs(closest))
else:
    print(closest)