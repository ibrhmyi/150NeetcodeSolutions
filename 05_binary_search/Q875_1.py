class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  # O(n* log(m)) Time complexity
        left, right = 1, max(piles)  # possible eating speeds

        while left < right:
            mid = (left + right) // 2
            hours = sum(-(-pile // mid) for pile in piles)

            if hours > h:
                left = mid + 1  # need to eat faster
            else:
                right = mid  # can try slower speed

        return left
