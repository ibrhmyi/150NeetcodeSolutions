class Solution:

    def isPalindrome(self, s: str) -> bool:   #SUPER SIMPLE BUT O(n) memory    
        s = list(re.sub(r'[^a-zA-Z0-9]', '', s).lower())
        if s == s[::-1]:
            return True 
        else:
            return False

  
    def isPalindrome2(self, s: str) -> bool:    #SLOW AF
        s = list(re.sub(r'[^a-zA-Z0-9]', '', s).lower())
        while len(s) > 1:
            if s[0] == s[-1]:
                del s[0]
                del s[-1]
            else:
                return False
        return True 


    def isPalindrome3(self, s: str) -> bool: #EVEN SLOWER
        l = 0
        r = len(s) - 1 

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l = l + 1
            r = r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


