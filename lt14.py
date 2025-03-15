class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans: str = ""
        i: int = ""
        hold: char = ""

        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return ""
        else:

            while i < len(strs):
                pass