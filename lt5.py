class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPal: str = 0

        for i in range(0,len(s)):
            oddPal: str = self.crawl(s,i,i)
            evenPal: str = self.crawl(s, i, i+1)
            
            if(len(oddPal) > len(maxPal)):
                maxPal = oddPal
            if(len(evenPal) > len(maxPal)):
                maxPal = evenPal

        return maxPal

    def crawl(self, s: str, left:int, right:int):
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1

        return s[left:right]