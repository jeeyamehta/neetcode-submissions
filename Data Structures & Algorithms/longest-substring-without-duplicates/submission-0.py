class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l, r = 0, 1
        longest = 1
        temp = s[l]
        while r<len(s):
            if s[r] in temp:
                l += 1
                temp = s[l:r]
            else:
                r+=1
                temp = s[l:r]
            longest = max(len(temp), longest)
                
        return longest
            