"""
arr = [2,3,4,5,6,7,8,9]

k=3

start=0

end = k+1

while 


"""

arr = [2,3,41,5,6,7,8,9]

k=4
largest = arr[0]
start=0
end = k

max_sum = 0

while end<len(arr):
    curr_sum = sum(arr[start:end])

    if curr_sum > max_sum:

        max_sum =curr_sum
        largest_start = start
        largest_end = end
    start +=1
    end+=1

print(largest_start,largest_end)


    


