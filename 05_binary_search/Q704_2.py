class Solution:
    def search(self, nums: List[int], target: int) -> int: #O(n), we need O(nlogn)
        if target in nums:
            return nums.index(target)
        else:
            return -1

        def search2(self, nums: List[int], target: int) -> int: #2 pointers
        l, r = 0, len(nums) -1
        while l <= r:
            m = (l+r) // 2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:  
                l = m + 1
            else:
                return m
        return -1



