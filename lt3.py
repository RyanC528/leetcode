class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars:set = set()
        ret:int = 0
        length:int = 0

        for i in range(0, len(s)):
            while s[i] in chars:
                chars.remove(s[length])
                length += 1
        chars.add(s[i])
        ret = max(ret, ret - length + 1)
      
        return ret