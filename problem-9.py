class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        
        y:int = 0
        hold: int = x

        while hold:
            y = y * 10 + hold % 10
            hold //= 10

        return x == y
    
    