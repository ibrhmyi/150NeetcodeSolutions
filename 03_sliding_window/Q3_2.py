class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  #with lists 

        mylist = []
        maxlenght = 0
        for l in s:
            if l in mylist:
                index = mylist.index(l)
                mylist = mylist[index + 1:]
            mylist.append(l)
            maxlenght = max(maxlenght, len(mylist))
        return maxlenght

  class Solution:          
    def lengthOfLongestSubstring(self, s: str) -> int: #with sets 

        myset = set()
        l = 0
        maxlenght = 0
        for i in range(len(s)):
            while s[i] in myset:
                myset.remove(s[l])
                l+=1
            myset.add(s[i])
            maxlenght = max(maxlenght, i - l +1)
        return maxlenght
