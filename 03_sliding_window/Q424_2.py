
class Solution: #SIMPLE
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = 0
        max_streak = 0

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            while (r-l+1) - max(counts.values())> k:
                counts[s[l]] -= 1
                l += 1
            max_streak = max(max_streak,r-l+1)
        return max_streak


class Solution: # FASTER
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = 0
        max_freq = 0
        max_streak = 0

        for r in range(len(s)):
            # 1. "If doesn't exist, generate; if exists, increment"
            char = s[r]
            counts[char] = counts.get(char, 0) + 1

            # Track the most frequent character in our current window
            max_freq = max(max_freq, counts[char])

            # Logic: If (window_size - max_freq) > k, we've used more than k replacements
            while (r-l+1) - max_freq > k:
                counts[s[l]] -= 1
                l += 1
            max_streak = max(max_streak,r-l+1)
        return max_streak


