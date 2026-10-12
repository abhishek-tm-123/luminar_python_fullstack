def containsDuplicate(nums: list[int]) -> bool:
        stack = set()
        for num in nums:
            if num not in stack:
                stack.add(num)
            else:
                return True
            
        return False

print(containsDuplicate([1,2,3,1]))