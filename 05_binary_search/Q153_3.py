class Solution:
    def findMin(self, nums: List[int]) -> int: # O(n2)
        while nums[0] > nums[-1]:
            del nums[0]
        return nums[0]
      

    def findMin2(self, nums: List[int]) -> int: #O(n)
        nums.reverse()
        while nums[-1] > nums[0]:
            nums.pop()
        return nums[-1]


    def findMin(self, nums: List[int]) -> int: #O(logn)
        l, r = 0, len(nums) -1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[r]
