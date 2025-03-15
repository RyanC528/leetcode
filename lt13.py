class Solution:
    def romanToInt(self, s: str) -> int:

        ans: int = 0
        i: int = 0
        key: dict = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

        while i < len(s):

            if i == len(s) - 1:
                ans += key[s[i]]
                i += 1

            else:

                if s[i:i+2] in key:
                    ans += key[s[i:i+2]]
                    i += 2
                else:
                    ans += key[s[i]]
                    i += 1

        return ans