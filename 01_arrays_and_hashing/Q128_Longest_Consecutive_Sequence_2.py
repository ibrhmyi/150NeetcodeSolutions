class Solution:
    def longestConsecutive1(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        
        sequence = []
        best = []
        for num in nums:
            if not sequence:
                sequence.append(num)
            elif num == (sequence[-1] +1):
                sequence.append(num)
            elif num == (sequence[-1]):
                continue
            else:
                best.append(len(sequence))
                sequence.clear()
                sequence.append(num)
                
        best.append(len(sequence))  
        best.sort(reverse=True)
        return best[0]


    def longestConsecutive2(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            if num - 1 not in numset:
                length = 0
                while num + length in numset:
                    length += 1
                longest = max(length, longest)
        return longest
