# classic kadene
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        listsum = nums[0]
        newsum = 0
        for num in nums:
            if newsum < 0:
                newsum = 0
            newsum += num
            listsum = max(newsum, listsum)
        return listsum

# FASTEST
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        largestSum = float('-inf')
        for num in nums:
            sum += num
            if largestSum < sum:
                largestSum = sum
            if(sum < 0): sum = 0
        return largestSum

