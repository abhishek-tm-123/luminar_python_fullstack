class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last =( m+n )-1
        i=m-1
        j=n-1
        
        while j>=0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last]=nums1[i]
                i-=1
                last-=1
            else:
                nums1[last]=nums2[j]
                j-=1
                last-=1
                
        
        
sol = Solution()
sol.merge(nums1 = [2, 2, 3, 0, 0, 0],m = 3,nums2 = [1, 5, 6],n = 3)

