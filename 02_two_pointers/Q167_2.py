class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: #O(n^2) terrible

        for i in range(len(numbers)):
            j = i + 1
            while j < len(numbers) and (numbers[i] + numbers[j]) < target:
                j += 1
            if j < len(numbers) and (numbers[i] + numbers[j]) == target:
                return [i+1,j+1]


    def twoSum2(self, numbers: List[int], target: int) -> List[int]: #SIMPLE O(n) and O(1) space
        l = 0
        r = len(numbers) - 1

        while l < r:
            if (numbers[l] + numbers[r]) > target:
                r -= 1
            elif (numbers[l] + numbers[r]) < target:
                l +=1
            else:
                return [l+1,r+1]
