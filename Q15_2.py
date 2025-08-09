class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:  #OPTIMAL
        output = []
        nums.sort()

        for i in range(len(nums)):

            if nums[i] > 0:
              break #earlystop 
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = 1 + i
            r = len(nums) - 1

            while l < r:

                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l +=1
                elif total > 0:
                    r -= 1
                else:
                    output.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1

        return output

  
    def threeSum2(self, nums: List[int]) -> List[List[int]]: #HASHMAP
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        output = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    output.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return output
