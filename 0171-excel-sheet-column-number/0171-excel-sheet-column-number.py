class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        d = {alphabets[i]: i+1 for i in range(26)}
        
        result = 0
        for ch in columnTitle:
            result = result * 26 + d[ch]
        
        return result