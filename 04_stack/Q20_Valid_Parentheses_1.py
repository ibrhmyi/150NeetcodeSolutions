class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #I'll use this stack
        opentoclose = {')':'(','}':'{',']':'['} # I need to map the bracets to their pairs

        for c in s:
            if c in opentoclose: #if closing bracet
                if stack and stack[-1] == opentoclose[c]: #if what I added previous was opening from the same type 
                    stack.pop() #remove the previous opening bracet
                else: 
                    return False #if it wasn't this is a false case bc overlapping
            else:
                stack.append(c) #most be an opening bracet then, add it
        
        return True if not stack else False #if my stack is empty it means I found pairs for all bracets so this condition is true 
