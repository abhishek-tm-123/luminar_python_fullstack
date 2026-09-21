"""
least positive missing integer

set arr as [1,2,3,5]

find min mun in arr 
 
find max num in arr

find sum of min num to max num and set as total

find sum of current arr and set as arr_sum

if total != arr_sum so there is difference then
    display missing number is total - arr_sum
else no missing
"""

arr = [1,2,3,5]

min_num = min(arr)
max_num = max(arr)

total = 0

for i in range(min_num,max_num+1):
    total+=i

arr_sum = sum(arr)

if total != arr_sum:
    print("missing element :",total-arr_sum)
else:
    print("no missing")