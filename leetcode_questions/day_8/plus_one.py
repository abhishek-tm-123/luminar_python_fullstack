class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result=[]
        carry_add=1
        for d in digits[::-1]:
            if d == 9 and carry_add == 1:
                result.append(0)
                carry_add=1
            else:
                result.append(d+carry_add)
                carry_add=0
        if carry_add==1:
            result.append(carry_add)
        return result[::-1]
    
sol1 = Solution()

print(sol1.plusOne([1,9,2]))

