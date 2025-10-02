class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = -1
        for i in range(len(haystack)):
            if haystack[i:(i+len(needle))] == needle:
                idx = i
                return idx
            else:
                idx = idx 
        return idx 