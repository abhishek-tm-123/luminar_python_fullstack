def twoSum( nums: list[int], target: int) -> list[int]:
        hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hashmap:
                return [hashmap[diff], i]

            hashmap[nums[i]] = i

        return []

            

print(twoSum([2,4,3,5,6,7],8))
