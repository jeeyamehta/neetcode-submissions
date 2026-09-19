class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l, r = 0, 1
        longest = 1
        temp = set()
        for r in range(len(s)):
            while s[r] in temp:
                temp.remove(s[l])
                l += 1
            temp.add(s[r])
            longest = max(len(temp), longest)
                
        return longest
            