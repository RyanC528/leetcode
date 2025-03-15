class Solution:
    def romanToInt(self, s: str) -> int:

        key: dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50, 
            "C" : 100, 
            "D" : 500,
            "M" : 1000,
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM"  : 900,
        }

        ans : int = 0
        hold : list =[]

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "I":
                if (s[i-1] == "V") or (s[i -1] == "X"):
                    hold.append(s[i] + s[i - 1])
                    i = i - 1
            elif s[i] == "X":
                if (s[i - 1] == "L") or (s[i - 1] == "C"):
                    hold.append(s[i] + s[i - 1])
                    i = i - 1
            elif s[i] == "C":
                if (s[i - 1] == "D") or (s[i - 1] == "M"):
                    hold.append(s[i] + s[i - 1])
                    i = i - 1
            else:
                hold.append(s[i])

        for item in hold:
            print(item)
            ans = ans + key[item]

        print(ans)


ob = Solution()
ob.romanToInt("MCMXCIV")
