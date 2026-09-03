"""
set pre to 0
set curr to 1
display pre
display curr
repeat for i from 1 to 11 then 
    calculate next as pre + curr
    display next
    update pre to curr
    update curr to next

"""

pre = 0
curr = 1
print(pre)
print(curr)
for i in range(1,11):
    next = pre + curr
    print(next)
    pre = curr
    curr = next
    
